# Etapa 5 — LLM Engineering, evaluación y entrenamiento

Semanas 33–40. Acá el portfolio se vuelve específico: no “usé ChatGPT”, sino “medí seis sistemas”.

## Formación

- Hugging Face: Transformers, PEFT, Datasets
- Documentación de PyTorch
- Cursos cortos de DeepLearning.AI sobre LLMs y evaluación
- Papers/docs de LoRA, QLoRA y evaluación generativa

## Conceptos

RAG, vector database, fine-tuning, LoRA, QLoRA, quantization, benchmark, hallucination, grounding, inference optimization.

## Proyecto central

[Benchmark de epicrisis](../proyectos/04-epicrisis-benchmark/README.md)

Compará:

1. Modelo comercial A (API)
2. Modelo comercial B
3. Modelo abierto, sin ajustes
4. Modelo abierto + prompting estructurado
5. Modelo abierto + LoRA
6. Modelo ajustado + recuperación y verificación de fuentes

No esperes que el ajustado gane en todo. Puede mejorar estructura y empeorar fidelidad; bajar costo y subir latencia. Tu trabajo es descubrirlo.

En paralelo: [Asistente de conocimiento](../proyectos/05-knowledge-assistant/README.md).
