"""Carga, split por paciente y preprocesamiento.

GroupShuffleSplit: ningún patient_id aparece a la vez en train y test.
Eso es el antídoto más simple contra un tipo frecuente de leakage.
"""

from __future__ import annotations

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .config import (
    GROUP_COL,
    LEAKY_FEATURES,
    SEED,
    TARGET_CLASSIFICATION,
    TARGET_REGRESSION,
    USABLE_CATEGORICAL,
    USABLE_NUMERIC,
)


def feature_columns(include_leaky: bool = False) -> tuple[list[str], list[str]]:
    numeric = list(USABLE_NUMERIC)
    categorical = list(USABLE_CATEGORICAL)
    if include_leaky:
        numeric = numeric + list(LEAKY_FEATURES)
    return numeric, categorical


def split_by_patient(df, test_size: float = 0.2, seed: int = SEED):
    splitter = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=seed)
    train_idx, test_idx = next(splitter.split(df, groups=df[GROUP_COL]))
    return df.iloc[train_idx].reset_index(drop=True), df.iloc[test_idx].reset_index(drop=True)


def assert_no_patient_overlap(train_df, test_df) -> None:
    overlap = set(train_df[GROUP_COL]).intersection(set(test_df[GROUP_COL]))
    if overlap:
        raise ValueError(f"Fuga por paciente: {len(overlap)} ids compartidos")


def make_preprocessor(include_leaky: bool = False) -> ColumnTransformer:
    numeric, categorical = feature_columns(include_leaky)
    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric),
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                categorical,
            ),
        ]
    )


def xy(df, include_leaky: bool = False):
    numeric, categorical = feature_columns(include_leaky)
    X = df[numeric + categorical]
    y_reg = df[TARGET_REGRESSION]
    y_clf = df[TARGET_CLASSIFICATION]
    groups = df[GROUP_COL]
    return X, y_reg, y_clf, groups


def wrap_model(estimator, include_leaky: bool = False) -> Pipeline:
    return Pipeline(
        steps=[
            ("prep", make_preprocessor(include_leaky)),
            ("model", estimator),
        ]
    )
