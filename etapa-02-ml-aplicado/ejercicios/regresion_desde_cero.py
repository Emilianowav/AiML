"""Regresión lineal ordinaria (OLS) implementada con NumPy.

La fórmula de la solución cerrada:

    w = (XᵀX)⁻¹ Xᵀ y

X incluye una columna de 1s para el intercepto.
No uses esto en producción: sirve para entender lo que scikit-learn oculta.
"""

from __future__ import annotations

import numpy as np


def add_intercept(X: np.ndarray) -> np.ndarray:
    ones = np.ones((X.shape[0], 1), dtype=float)
    return np.hstack([ones, X])


def fit_ols(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    Xb = add_intercept(X)
    xtx = Xb.T @ Xb
    xty = Xb.T @ y
    return np.linalg.solve(xtx, xty)


def predict_ols(X: np.ndarray, weights: np.ndarray) -> np.ndarray:
    return add_intercept(X) @ weights


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(np.abs(y_true - y_pred)))


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    n = 200
    edad = rng.normal(65, 12, n)
    icc = rng.binomial(1, 0.25, n)
    # Días de internación simulados: base 4, +edad, +ICC, ruido.
    y = 4 + 0.05 * (edad - 60) + 2.5 * icc + rng.normal(0, 1.0, n)
    X = np.column_stack([edad, icc])

    weights = fit_ols(X, y)
    pred = predict_ols(X, weights)

    print("Pesos [intercepto, edad, icc]:", np.round(weights, 3))
    print(f"MAE: {mae(y, pred):.3f}  RMSE: {rmse(y, pred):.3f}")
    print("El peso de ICC debería acercarse a +2.5 días.")
