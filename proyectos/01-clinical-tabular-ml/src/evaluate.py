"""Métricas de regresión y clasificación, con intervalo de confianza bootstrap."""

from __future__ import annotations

import numpy as np
from sklearn.calibration import calibration_curve
from sklearn.metrics import (
    average_precision_score,
    brier_score_loss,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    precision_score,
    r2_score,
    recall_score,
    roc_auc_score,
)


def _bootstrap_ci(y_true, y_score, metric_fn, n_boot: int = 400, seed: int = 42):
    rng = np.random.default_rng(seed)
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)
    n = len(y_true)
    stats = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        try:
            stats.append(metric_fn(y_true[idx], y_score[idx]))
        except ValueError:
            continue
    if not stats:
        return (float("nan"), float("nan"))
    low, high = np.percentile(stats, [2.5, 97.5])
    return (float(low), float(high))


def regression_metrics(y_true, y_pred) -> dict:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    r2 = r2_score(y_true, y_pred)
    mae_ci = _bootstrap_ci(y_true, y_pred, mean_absolute_error)
    return {
        "mae": float(mae),
        "mae_ci_low": mae_ci[0],
        "mae_ci_high": mae_ci[1],
        "rmse": rmse,
        "r2": float(r2),
    }


def classification_metrics(y_true, y_prob, threshold: float = 0.5) -> dict:
    y_true = np.asarray(y_true, dtype=int)
    y_prob = np.asarray(y_prob, dtype=float)
    y_pred = (y_prob >= threshold).astype(int)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    try:
        roc = roc_auc_score(y_true, y_prob)
    except ValueError:
        roc = float("nan")
    pr = average_precision_score(y_true, y_prob)
    brier = brier_score_loss(y_true, y_prob)
    return {
        "precision": float(prec),
        "recall": float(rec),
        "f1": float(f1),
        "roc_auc": float(roc),
        "pr_auc": float(pr),
        "brier": float(brier),
        "prevalence": float(y_true.mean()),
    }


def calibration_points(y_true, y_prob, n_bins: int = 8):
    frac, mean_pred = calibration_curve(y_true, y_prob, n_bins=n_bins, strategy="quantile")
    return mean_pred, frac
