from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import PrecisionRecallDisplay, RocCurveDisplay

from .evaluate import calibration_points


def plot_pred_vs_true(y_true, predictions: dict, path) -> None:
    n = len(predictions)
    fig, axes = plt.subplots(1, n, figsize=(4.2 * n, 4), squeeze=False)
    y_true = np.asarray(y_true)
    for ax, (name, pred) in zip(axes[0], predictions.items()):
        ax.scatter(y_true, pred, alpha=0.25, s=12)
        lo, hi = y_true.min(), y_true.max()
        ax.plot([lo, hi], [lo, hi], color="black", linewidth=1)
        ax.set_title(name)
        ax.set_xlabel("Días reales")
        ax.set_ylabel("Días predichos")
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)


def plot_roc_pr(y_true, probabilities: dict, roc_path, pr_path) -> None:
    fig, ax = plt.subplots(figsize=(5.5, 5))
    for name, prob in probabilities.items():
        RocCurveDisplay.from_predictions(y_true, prob, name=name, ax=ax)
    ax.set_title("ROC — internación prolongada")
    fig.tight_layout()
    fig.savefig(roc_path, dpi=140)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(5.5, 5))
    for name, prob in probabilities.items():
        PrecisionRecallDisplay.from_predictions(y_true, prob, name=name, ax=ax)
    ax.set_title("Precision-Recall — internación prolongada")
    fig.tight_layout()
    fig.savefig(pr_path, dpi=140)
    plt.close(fig)


def plot_calibration(y_true, probabilities: dict, path) -> None:
    fig, ax = plt.subplots(figsize=(5.5, 5))
    ax.plot([0, 1], [0, 1], "--", color="gray", label="perfecto")
    for name, prob in probabilities.items():
        x, y = calibration_points(y_true, prob)
        ax.plot(x, y, marker="o", label=name)
    ax.set_xlabel("Probabilidad media predicha")
    ax.set_ylabel("Frecuencia real")
    ax.set_title("Calibración")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
