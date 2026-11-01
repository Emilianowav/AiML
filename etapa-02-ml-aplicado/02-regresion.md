# Regresión lineal

## Idea

Querés un número: días de internación, precio, hemoglobina futura. El modelo lineal dice: *y* es una suma ponderada de las features más un sesgo.

```text
días ≈ b0 + b1·edad + b2·insuficiencia_cardiaca + b3·urgencia + …
```

No es “la verdad biológica”. Es una aproximación interpretable y un baseline obligatorio.

## Lo que tenés que entender, no memorizar

- **Residual:** lo que el modelo no explicó (`real - predicho`).
- **MAE:** error absoluto medio. Se lee en días. Es la métrica más honesta para hablar con no técnicos.
- **RMSE:** penaliza más los errores grandes (una internación predicha 2 días que duró 20).
- **R²:** fracción de varianza explicada. Puede verse bien y aun así ser inútil si el error en días es alto.
- **Regularización (Ridge/Lasso):** evita coeficientes locos cuando hay muchas variables correlacionadas.

## Split

Si mezclás internaciones del mismo paciente entre train y test, el modelo “conoce” a esa persona. En salud, el corte correcto casi siempre es **por paciente** o **por tiempo**.

## Relación con Zoomcamp

El módulo 2 predice precio de autos. El ejercicio es el mismo; cambian las columnas. Implementá OLS a mano en `ejercicios/regresion_desde_cero.py` y después usá scikit-learn en el proyecto.

## Tarea

Correr el pipeline clínico y anotar el MAE del modelo lineal. Ese número es tu baseline. Forest y XGBoost tienen que ganarle de forma estable, no por 0.01 días.
