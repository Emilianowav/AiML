"""Métricas de clasificación escritas a mano.

TP = verdaderos positivos (dijimos sí, era sí)
FP = falsos positivos     (dijimos sí, era no)
FN = falsos negativos     (dijimos no, era sí)
TN = verdaderos negativos (dijimos no, era no)

precision = TP / (TP + FP)
recall    = TP / (TP + FN)
F1        = 2 * precision * recall / (precision + recall)
"""

from __future__ import annotations

import numpy as np


def confusion(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, int]:
    y_true = np.asarray(y_true).astype(int)
    y_pred = np.asarray(y_pred).astype(int)
    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn}


def precision_recall_f1(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    c = confusion(y_true, y_pred)
    prec = c["tp"] / (c["tp"] + c["fp"]) if (c["tp"] + c["fp"]) else 0.0
    rec = c["tp"] / (c["tp"] + c["fn"]) if (c["tp"] + c["fn"]) else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
    acc = (c["tp"] + c["tn"]) / max(len(y_true), 1)
    return {"precision": prec, "recall": rec, "f1": f1, "accuracy": acc, **c}


if __name__ == "__main__":
    # 10 internaciones: 3 prolongadas. Un modelo cobarde que nunca alerta.
    y_true = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1])
    nunca_alerta = np.zeros_like(y_true)
    m = precision_recall_f1(y_true, nunca_alerta)
    print("Modelo que siempre dice 'no prolongada':")
    print(f"  accuracy={m['accuracy']:.2f}  recall={m['recall']:.2f}  precision={m['precision']:.2f}")
    print("Accuracy alta, recall cero: así miente el accuracy con desbalance.")
