# E. Cómo se investiga y mejora un modelo

Sin estos conceptos, los proyectos A y B son demos. Con ellos, son investigación aplicada.

## Benchmark

- **Qué significa:** conjunto de pruebas comparable entre sistemas.
- **Qué problema resuelve:** dejar de discutir opiniones.
- **Ejemplo médico:** 80 notas sintéticas con JSON de referencia para extracción clínica.

## Baseline

- **Qué significa:** resultado de referencia contra el que medís mejoras.
- **Qué problema resuelve:** saber si LoRA valió la pena.
- **Ejemplo médico:** prompt simple sobre un modelo abierto, antes de RAG, antes de fine-tuning.

## Ablation study

- **Qué significa:** sacar una parte del sistema y medir cuánto aportaba.
- **Qué problema resuelve:** no acumular componentes de adorno.
- **Ejemplo médico:** apagar el reranker y ver si la precisión del asistente cae 2 puntos o 20.

## Error analysis

- **Qué significa:** mirar casos fallidos de forma sistemática (por tipo de error, no uno por uno al azar).
- **Qué problema resuelve:** mejorar lo que importa.
- **Ejemplo médico:** agrupar fallos de epicrisis en “omitió alergia”, “inventó fecha”, “rompió el JSON”.

## Data drift

- **Qué significa:** los datos de entrada cambian respecto al entrenamiento.
- **Qué problema resuelve:** detectar que el mundo se movió.
- **Ejemplo médico:** cambia el formulario de admisión y `n_medications` deja de cargarse: el modelo de estadía se degrada.

## Model drift

- **Qué significa:** el comportamiento del modelo empeora en el tiempo (por drift de datos, de etiquetas o de uso).
- **Qué problema resuelve:** no asumir que un `.pkl` de marzo sigue valiendo en noviembre.
- **Ejemplo médico:** Evidently alerta que el MAE de internación subió después de un cambio de protocolo quirúrgico.

## Reproducibility

- **Qué significa:** repetir el experimento y obtener resultados comparables (semilla, versiones, splits).
- **Qué problema resuelve:** “en mi máquina daba otra cosa”.
- **Ejemplo médico:** `run_pipeline.py` con `seed=42` y corte por `patient_id` versionado.

## Experiment tracking

- **Qué significa:** registrar configuraciones, datos, código y métricas.
- **Qué problema resuelve:** no perder la corrida que sí funcionó.
- **Ejemplo médico:** MLflow con modelo, MAE, split y commit de git del servicio de predicción.

## Hallucination

- **Qué significa:** contenido generado sin respaldo suficiente.
- **Qué problema resuelve:** nombrarlo para medirlo; no se elimina solo con “un modelo más grande”.
- **Ejemplo médico:** la epicrisis menciona una hemoglobina que no está en ninguna nota.

## Grounding

- **Qué significa:** vincular cada afirmación a información verificable.
- **Qué problema resuelve:** poder auditar.
- **Ejemplo médico:** cada diagnóstico en el JSON apunta a un fragmento de la evolución.
