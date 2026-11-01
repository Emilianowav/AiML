# Programa completo

Este documento es el mapa de las etapas 2 a 7. La formación conceptual (el glosario) corre en paralelo, no al final.

## Etapa 2 — Machine Learning aplicado y evaluación estadística

**Semanas 9–16** · carpeta [`etapa-02-ml-aplicado`](../etapa-02-ml-aplicado/README.md)

Pasás de entender algoritmos a saber elegirlos y evaluarlos.

**Formación**

1. Completar y profundizar la especialización de Andrew Ng.
2. Complementar con [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp).

**Temas**

Regresión lineal y logística, árboles, Random Forest, Gradient Boosting, XGBoost/CatBoost, clustering, reducción de dimensionalidad, feature engineering, selección de variables, validación cruzada, desbalance de clases, data leakage, interpretabilidad, calibración de probabilidades.

**Estadística que no se puede ignorar**

| Concepto | Por qué importa |
| --- | --- |
| Precision | Cuántas predicciones positivas son correctas |
| Recall | Cuántos positivos reales detecta |
| F1 | Equilibrio entre precision y recall |
| ROC-AUC | Capacidad de discriminación |
| PR-AUC | Rendimiento cuando hay clases desbalanceadas |
| Calibration | Si las probabilidades predichas son confiables |
| Confidence interval | Cuánta incertidumbre tiene una métrica |

**Proyecto:** [Clinical Tabular ML](../proyectos/01-clinical-tabular-ml/README.md)

## Etapa 3 — Deep Learning y PyTorch

**Semanas 17–24** · carpeta [`etapa-03-deep-learning`](../etapa-03-deep-learning/README.md)

Curso: Deep Learning Specialization. Complemento: tutoriales oficiales de PyTorch.

Tenés que escribir a mano Dataset, DataLoader, arquitectura, loss, optimizador, loop de entrenamiento, loop de validación, guardado y carga. No alcanza con `model.fit()`.

**Proyecto:** [Redes en PyTorch](../proyectos/02-pytorch-redes/README.md)

## Etapa 4 — NLP, Transformers y arquitectura de LLMs

**Semanas 25–32** · carpeta [`etapa-04-nlp-transformers`](../etapa-04-nlp-transformers/README.md)

Curso: Hugging Face NLP Course.

Conceptos: tokenización, embedding, attention, Transformer, pretraining, inference, context window, fine-tuning.

**Proyecto:** [Extracción clínica](../proyectos/03-extraccion-clinica/README.md)

## Etapa 5 — LLM Engineering, evaluación y entrenamiento

**Semanas 33–40** · carpeta [`etapa-05-llm-engineering`](../etapa-05-llm-engineering/README.md)

RAG, vector database, LoRA, QLoRA, quantization, benchmarks, hallucination, grounding, inference optimization.

**Proyecto central:** [Benchmark de epicrisis](../proyectos/04-epicrisis-benchmark/README.md)

También avanza [Asistente de conocimiento](../proyectos/05-knowledge-assistant/README.md).

## Etapa 6 — MLOps, despliegue y producción

**Semanas 41–48** · carpeta [`etapa-06-mlops`](../etapa-06-mlops/README.md)

Curso: MLOps Zoomcamp. Herramientas: MLflow, Docker, FastAPI, Evidently, GitHub Actions, PostgreSQL.

**Proyecto:** [Servicio MLOps](../proyectos/06-mlops-servicio/README.md)

## Etapa 7 — Consolidación y preparación laboral

**Semanas 49–52** · carpeta [`etapa-07-consolidacion`](../etapa-07-consolidacion/README.md)

Documentación, repos, portfolio, LinkedIn, CV bilingüe, ejercicios técnicos, informe del benchmark de epicrisis.
