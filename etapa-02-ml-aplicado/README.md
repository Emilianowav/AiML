# Etapa 2 — Machine Learning aplicado y evaluación estadística

Semanas 9–16. Objetivo: dejar de “conocer algoritmos” y pasar a **elegirlos y evaluarlos**.

## Cursos

1. Profundizar la [Machine Learning Specialization de Andrew Ng](https://www.coursera.org/specializations/machine-learning-introduction).
2. Seguir [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) módulo a módulo.

Cohorte 2026: https://courses.datatalks.club/ml-zoomcamp-2026/

## Cómo usar Zoomcamp desde acá

No copies el repositorio del curso a tu portfolio. Hacé esto, en orden:

1. Mirá la clase oficial (GitHub + video).
2. Leé la nota en español de esta carpeta.
3. Resolvé el homework en una rama o carpeta local que **no** publiques como proyecto.
4. Aplicá la idea al [Clinical Tabular ML](../proyectos/01-clinical-tabular-ml/README.md).

## Mapa Zoomcamp → esta etapa

| Módulo Zoomcamp | Nota acá | Qué llevás al proyecto clínico |
| --- | --- | --- |
| 1. Introducción y CRISP-DM | [01-introduccion.md](01-introduccion.md) | Definir el problema: predecir días de internación |
| 2. Regresión | [02-regresion.md](02-regresion.md) | Baseline lineal + error MAE/RMSE |
| 3. Clasificación | [03-clasificacion.md](03-clasificacion.md) | Internación prolongada (sí/no) |
| 4. Evaluación | [04-evaluacion.md](04-evaluacion.md) | Precision, recall, F1, ROC-AUC, PR-AUC, calibración, IC |
| 5. Deploy | se retoma en Etapa 6 | No distraigas el midterm de evaluación |
| 6. Árboles y boosting | [05-arboles-ensambles.md](05-arboles-ensambles.md) | Random Forest vs XGBoost |
| Extra del programa | [06-features-clustering.md](06-features-clustering.md) | Leakage, features, clustering, dimensionalidad |

## Ejercicios propios (estos sí van al repo)

- [ejercicios/regresion_desde_cero.py](ejercicios/regresion_desde_cero.py) — OLS con NumPy.
- [ejercicios/metricas_desde_cero.py](ejercicios/metricas_desde_cero.py) — matriz de confusión, precision, recall, F1.

## Entregable de la etapa

Un modelo entrenado, una evaluación estadística y un informe que justifique qué algoritmo elegirías y por qué.

Eso ya está cableado en `proyectos/01-clinical-tabular-ml`. Tu trabajo es entender cada número y reescribir el informe con criterio clínico, no dejar el texto generado tal cual.
