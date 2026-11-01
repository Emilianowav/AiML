"""Entrena Ridge, Random Forest y XGBoost y escribe la evaluación.

Uso:
    python run_pipeline.py
    python run_pipeline.py --leaky   # demo de data leakage (no usar en el informe)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from joblib import dump
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, Ridge
from xgboost import XGBClassifier, XGBRegressor

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.config import FIGURES_DIR, MODELS_DIR, SEED  # noqa: E402
from src.dataset import (  # noqa: E402
    assert_no_patient_overlap,
    split_by_patient,
    wrap_model,
    xy,
)
from src.evaluate import classification_metrics, regression_metrics  # noqa: E402
from src.generate_data import save_raw_dataset  # noqa: E402
from src.plots import plot_calibration, plot_pred_vs_true, plot_roc_pr  # noqa: E402
from src.report import write_informe, write_metrics_json  # noqa: E402


def build_regressors():
    return {
        "ridge": Ridge(alpha=1.0),
        "random_forest": RandomForestRegressor(
            n_estimators=200,
            min_samples_leaf=4,
            random_state=SEED,
            n_jobs=-1,
        ),
        "xgboost": XGBRegressor(
            n_estimators=250,
            learning_rate=0.05,
            max_depth=4,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=SEED,
            n_jobs=-1,
            verbosity=0,
        ),
    }


def build_classifiers():
    return {
        "logistica": LogisticRegression(max_iter=1000, class_weight="balanced"),
        "random_forest": RandomForestClassifier(
            n_estimators=200,
            min_samples_leaf=4,
            random_state=SEED,
            n_jobs=-1,
            class_weight="balanced",
        ),
        "xgboost": XGBClassifier(
            n_estimators=250,
            learning_rate=0.05,
            max_depth=4,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=SEED,
            n_jobs=-1,
            eval_metric="logloss",
            verbosity=0,
        ),
    }


def main(include_leaky: bool = False) -> None:
    df = save_raw_dataset()
    train_df, test_df = split_by_patient(df)
    assert_no_patient_overlap(train_df, test_df)

    X_train, y_reg_train, y_clf_train, _ = xy(train_df, include_leaky)
    X_test, y_reg_test, y_clf_test, _ = xy(test_df, include_leaky)

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    reg_preds = {}
    reg_metrics = {}
    for name, estimator in build_regressors().items():
        pipe = wrap_model(estimator, include_leaky)
        pipe.fit(X_train, y_reg_train)
        pred = pipe.predict(X_test)
        reg_preds[name] = pred
        reg_metrics[name] = regression_metrics(y_reg_test, pred)
        dump(pipe, MODELS_DIR / f"reg_{name}.joblib")
        print(f"[regresión] {name:15} MAE={reg_metrics[name]['mae']:.3f}")

    clf_probs = {}
    clf_metrics = {}
    for name, estimator in build_classifiers().items():
        pipe = wrap_model(estimator, include_leaky)
        pipe.fit(X_train, y_clf_train)
        if hasattr(pipe.named_steps["model"], "predict_proba"):
            prob = pipe.predict_proba(X_test)[:, 1]
        else:
            prob = pipe.predict(X_test)
        clf_probs[name] = prob
        clf_metrics[name] = classification_metrics(y_clf_test, prob)
        dump(pipe, MODELS_DIR / f"clf_{name}.joblib")
        print(f"[clasif.   ] {name:15} PR-AUC={clf_metrics[name]['pr_auc']:.3f}")

    plot_pred_vs_true(y_reg_test, reg_preds, FIGURES_DIR / "pred_vs_true.png")
    plot_roc_pr(y_clf_test, clf_probs, FIGURES_DIR / "roc.png", FIGURES_DIR / "pr.png")
    plot_calibration(y_clf_test, clf_probs, FIGURES_DIR / "calibration.png")

    payload = {
        "include_leaky": include_leaky,
        "n_patients": int(df["patient_id"].nunique()),
        "n_encounters": int(len(df)),
        "n_train": int(len(train_df)),
        "n_test": int(len(test_df)),
        "prevalence": float(df["prolonged_stay"].mean()),
        "regression": reg_metrics,
        "classification": clf_metrics,
    }
    write_metrics_json(payload)
    write_informe(payload)
    print("Listo: reports/INFORME.md")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--leaky",
        action="store_true",
        help="Incluye features de alta (demo de leakage). No uses esto en el informe.",
    )
    args = parser.parse_args()
    main(include_leaky=args.leaky)
