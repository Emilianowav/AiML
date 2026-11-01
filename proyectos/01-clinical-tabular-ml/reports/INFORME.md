# Informe — Clinical Tabular ML

Fecha: 2026-11-01

## Problema

Estimar días de internación al ingreso (o con datos tempranos) sobre un dataset sintético.
El conjunto de prueba se separó **por paciente** para no mezclar internaciones de la misma persona.

## Datos

- Pacientes: 1800
- Internaciones: 3622
- Train / test: 2908 / 714
- Prevalencia de internación ≥ 7 días: 36.0%

## Regresión (días de internación)

| Modelo | MAE | IC 95% MAE | RMSE | R² |
| --- | --- | --- | --- | --- |
| ridge | 0.974 | [0.926, 1.026] | 1.197 | 0.662 |
| random_forest | 1.059 | [1.006, 1.118] | 1.310 | 0.595 |
| xgboost | 1.013 | [0.959, 1.065] | 1.245 | 0.635 |

**Menor MAE en test:** `ridge`.

## Clasificación (internación prolongada)

| Modelo | Precision | Recall | F1 | ROC-AUC | PR-AUC | Brier |
| --- | --- | --- | --- | --- | --- | --- |
| logistica | 0.682 | 0.806 | 0.739 | 0.888 | 0.832 | 0.139 |
| random_forest | 0.690 | 0.760 | 0.723 | 0.861 | 0.756 | 0.152 |
| xgboost | 0.774 | 0.678 | 0.723 | 0.876 | 0.801 | 0.135 |

## Qué modelo elegiría y por qué

Elegiría **Ridge**.

En test, Ridge tiene MAE 0.97 días (IC 95% 0.93–1.03). XGBoost queda en 1.01 y Random Forest en 1.06. Los intervalos se pisan: no hay evidencia de que el boosting gane. El proceso generador de estos datos es casi lineal (edad, comorbilidades, urgencia, cirugía), así que un modelo lineal regularizado es el más honesto.

En clasificación de internación prolongada, la logística tiene el mejor PR-AUC (0.83) y un recall alto (0.81). XGBoost sube precision (0.77) a costa de recall (0.68). Si el costo de no detectar una internación larga es mayor que el de una alarma de más, me quedo con logística y un umbral definido en validación, no en 0.5 por defecto.

No usé `billing_los_code` ni `n_notes_during_stay`: son variables de alta. Ganar MAE con ellas sería leakage.

Este párrafo es el borrador del primer run. Reescribilo cuando cambies datos, umbral o features.

## Limitaciones

- Datos sintéticos: las relaciones fueron diseñadas. Un dataset real (MIMIC, UCI diabetes 130) puede cambiar el ranking.
- No hay corte temporal: en un hospital real, entrenarías con internaciones viejas y testearías con las nuevas.
- No hay costos clínicos explícitos (cama vs. alarma) para elegir umbral.

## Figuras

- `figures/pred_vs_true.png`
- `figures/roc.png`
- `figures/pr.png`
- `figures/calibration.png`
