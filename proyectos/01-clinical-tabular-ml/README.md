# Clinical Tabular ML

Estimación de **duración de internación** a partir de datos tabulares clínicos.

Dataset sintético (publicable, sin PHI). El corte de train/test es **por paciente**, no por fila.

## English summary

Trains and compares Ridge, Random Forest and XGBoost to estimate hospital length of stay. Patient-level splits avoid leakage. Reports MAE with bootstrap confidence intervals, plus a secondary delayed-stay classifier (precision, recall, F1, ROC-AUC, PR-AUC, calibration).

## Problema

Al ingreso (o con datos disponibles temprano) queremos un número: **días de internación**. Sirve para camas, comunicación y como laboratorio de evaluación estadística.

Comparación mínima del programa:

- Regresión lineal (Ridge)
- Random Forest
- XGBoost

Tarea secundaria: clasificar internación prolongada (≥ 7 días) para practicar las métricas que no se pueden ignorar.

## Cómo correrlo

Desde la raíz del repo:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd proyectos\01-clinical-tabular-ml
python run_pipeline.py
python -m pytest tests
```

Salidas:

- `data/raw/encounters.csv` — datos sintéticos
- `models/*.joblib` — pipelines entrenados
- `reports/metrics.json` — números
- `reports/figures/` — gráficos
- `reports/INFORME.md` — borrador del informe (reescribilo vos)

## Diseño que importa en una entrevista

1. **Unidad de split:** `patient_id`. Si Ana tiene 3 internaciones, las tres van juntas.
2. **Leakage controlado:** `billing_los_code` y `n_notes_during_stay` existen en el CSV y se excluyen. Activalas una vez para ver un MAE “mágico” e inválido.
3. **Baseline primero:** Ridge. Forest y XGBoost tienen que ganarle en test, no en train.
4. **Incertidumbre:** MAE con intervalo de confianza bootstrap.
5. **Calibración:** en la tarea de internación prolongada, una probabilidad de 0.3 tiene que ocurrir cerca del 30%.

## Columnas

Usables al momento de predecir: edad, sexo, BMI, signos, laboratorios, comorbilidades, servicio, tipo de admisión, internaciones previas, medicación al ingreso.

Leaks (no usar): código de facturación correlacionado con la estadía, cantidad de notas escritas *durante* toda la internación.

## Cómo hablar de esto

No digas “XGBoost ganó”. En la primera corrida, **Ridge gana**. Eso es una lección, no un bug: si el fenómeno es casi lineal, el boosting no merece la complejidad.

Decí: “con corte por paciente, Ridge estima la estadía con MAE de ~1 día; Forest y XGBoost no mejoran de forma estable; no usé variables de alta.”
