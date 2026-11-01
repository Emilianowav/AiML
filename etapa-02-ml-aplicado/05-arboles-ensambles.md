# Árboles, Random Forest y Gradient Boosting

## Decision Tree

Parte el espacio de features con preguntas (“¿edad > 72?”, “¿hay ICC?”). Es interpretable y fácil de sobreajustar: un árbol profundo memoriza pacientes.

## Random Forest

Muchos árboles, cada uno ve un subconjunto de datos y de variables. Promedian. Baja la varianza. Sigue siendo fuerte en tabulares.

## Gradient Boosting (XGBoost, CatBoost)

Árboles en secuencia: cada uno corrige el error del anterior. Suele ganar en tablas. También es el primero que sobreajusta si lo alimentás con una feature filtrada.

CatBoost trata categorías nativamente. XGBoost es el estándar de portfolio. En este proyecto usamos XGBoost para tener una comparación clara con Forest y lineal.

## Cómo elegir

No elijas “el de mayor R² en train”. Elegí:

1. Mejor MAE (o PR-AUC) en test de pacientes no vistos.
2. Intervalo de confianza que no se pise con el baseline de forma vergonzosa.
3. Si el lineal pierde poco, quedate con el lineal: se explica en un comité de historia clínica.

## Relación con Zoomcamp

Módulo 6. El midterm del Zoomcamp puede ser este mismo proyecto clínico: dataset, EDA, modelos, evaluación y, más adelante, un FastAPI.

## Tarea

Mirá importancias. Si el ganador depende de `billing_los_code` o `n_notes_during_stay`, apagalas. Ganar con leakage no es ganar.
