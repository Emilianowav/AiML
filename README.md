# AiML — Machine Learning, Deep Learning y LLM Engineering

Formación práctica para diseñar, entrenar, evaluar y desplegar modelos, con foco en problemas clínicos y en productos de IA.

Este repositorio no es una copia de un curso. Es **tu workspace de aprendizaje y portfolio**: notas en español, ejercicios, un glosario aplicado a una plataforma médica, y proyectos que se pueden mostrar en LinkedIn y en búsquedas laborales.

> **English:** Practical ML/DL/LLM portfolio focused on healthcare. Start with [Clinical Tabular ML](proyectos/01-clinical-tabular-ml/README.md). Learning notes are in Spanish; project READMEs are bilingual.

---

## Qué vas a poder demostrar

Al terminar el programa deberías poder mostrar, con código y un informe:

1. Elegir un algoritmo y justificarlo con métricas, no con intuición.
2. Entrenar redes en PyTorch sin esconder el loop de entrenamiento.
3. Extraer información clínica estructurada con Transformers.
4. Comparar modelos de lenguaje con un benchmark honesto (costo, latencia, fidelidad).
5. Desplegar un modelo como servicio reproducible.

## Proyectos de portfolio

| # | Proyecto | Etapa | Estado | Qué demuestra |
| --- | --- | --- | --- | --- |
| 1 | [Clinical Tabular ML](proyectos/01-clinical-tabular-ml/README.md) | 2 | Listo para ejecutar | Regresión, Random Forest, XGBoost, split por paciente, métricas y calibración |
| 2 | [Redes en PyTorch](proyectos/02-pytorch-redes/README.md) | 3 | Plantilla | Dataset, DataLoader, arquitectura, loss, optimizador, loops, guardado |
| 3 | [Extracción clínica NLP](proyectos/03-extraccion-clinica/README.md) | 4 | Plantilla | Tokenización, prompting, JSON estructurado, citas a la fuente |
| 4 | [Benchmark de epicrisis](proyectos/04-epicrisis-benchmark/README.md) | 5 | Plantilla | RAG, LoRA, factualidad, omisiones, costo y latencia |
| 5 | [Asistente de conocimiento](proyectos/05-knowledge-assistant/README.md) | 4–5 | Plantilla | Retrieval, grounding, abstención, chunking y reranking |
| 6 | [Servicio MLOps](proyectos/06-mlops-servicio/README.md) | 6 | Plantilla | FastAPI, Docker, registro de modelo, monitoreo |

El proyecto 1 ya corre de punta a punta. El resto está especificado para construirse en las etapas siguientes, no como carpetas vacías.

## Cómo empezar (hoy)

```powershell
cd C:\Users\Emiliano\Desktop\AiML
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd proyectos\01-clinical-tabular-ml
python run_pipeline.py
python -m pytest tests
```

Eso genera datos clínicos sintéticos, entrena tres modelos, evalúa con intervalo de confianza y escribe un informe en `reports/INFORME.md`.

## Mapa del programa

| Etapa | Semanas | Carpeta | Curso ancla |
| --- | --- | --- | --- |
| 2. ML aplicado y evaluación | 9–16 | [etapa-02-ml-aplicado](etapa-02-ml-aplicado/README.md) | [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) + especialización de Andrew Ng |
| 3. Deep Learning y PyTorch | 17–24 | [etapa-03-deep-learning](etapa-03-deep-learning/README.md) | [Deep Learning Specialization](https://www.deeplearning.ai/courses/deep-learning-specialization/) |
| 4. NLP, Transformers y LLMs | 25–32 | [etapa-04-nlp-transformers](etapa-04-nlp-transformers/README.md) | [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) |
| 5. LLM Engineering | 33–40 | [etapa-05-llm-engineering](etapa-05-llm-engineering/README.md) | Hugging Face PEFT, LoRA/QLoRA, evaluación generativa |
| 6. MLOps | 41–48 | [etapa-06-mlops](etapa-06-mlops/README.md) | [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) |
| 7. Consolidación laboral | 49–52 | [etapa-07-consolidacion](etapa-07-consolidacion/README.md) | Portfolio, CV, entrevistas |

El glosario vive en [`glosario/`](glosario/README.md). La regla es siempre la misma: **qué significa, qué problema resuelve, y un ejemplo de la plataforma médica**.

## Relación con Machine Learning Zoomcamp

[DataTalks.Club Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) es el curso práctico de la Etapa 2. La cohorte 2026 corre de septiembre 2026 a enero 2027.

Este repo **no clona ni reescribe el curso**. Hace tres cosas distintas:

1. Te apunta a las clases oficiales, videos y homeworks.
2. Explica los mismos temas en español, con ejemplos clínicos.
3. Convierte lo aprendido en un proyecto propio (`Clinical Tabular ML`) que sí es material de portfolio.

Usá Zoomcamp para aprender. Usá este repositorio para entender, practicar y publicar tu trabajo.

- Curso: https://courses.datatalks.club/ml-zoomcamp-2026/
- Materiales: https://github.com/DataTalksClub/machine-learning-zoomcamp
- Videos: https://www.youtube.com/playlist?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR

## Estructura

```text
AiML/
├── docs/                      # Programa, método de estudio, LinkedIn
├── glosario/                  # Vocabulario aplicado a salud digital
├── etapa-02-ml-aplicado/      # Notas y ejercicios de la etapa actual
├── etapa-03-deep-learning/
├── etapa-04-nlp-transformers/
├── etapa-05-llm-engineering/
├── etapa-06-mlops/
├── etapa-07-consolidacion/
└── proyectos/                 # Lo que se muestra en entrevistas
```

## Principio de trabajo

Una red neuronal no es una colección de reglas escritas a mano. Vos definís una arquitectura, le das ejemplos y una función de pérdida; el entrenamiento ajusta los parámetros para reducir esa pérdida.

Esa diferencia —programar una solución versus entrenar un modelo— recorre todo el programa.

## Créditos

Los cursos y comunidades que estructuran esta formación:

- [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) — DataTalks.Club
- [Deep Learning Specialization](https://www.deeplearning.ai/courses/deep-learning-specialization/) — DeepLearning.AI / Andrew Ng
- [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course)
- [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp)
- [PyTorch tutorials](https://pytorch.org/tutorials/)

El contenido original de este repositorio (notas, ejercicios, datos sintéticos y proyectos) es independiente de esos cursos.
