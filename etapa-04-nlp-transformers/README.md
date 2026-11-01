# Etapa 4 — NLP, Transformers y arquitectura de LLMs

Semanas 25–32. Conecta de forma directa con trabajo sobre notas clínicas y documentación de un HIS.

## Curso

- [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) (Transformers, Datasets, Tokenizers, Accelerate).
- Módulos de atención/secuencias de la Deep Learning Specialization.
- Tutoriales de PyTorch sobre texto.

## Conceptos

Tokenización, embedding, attention, Transformer, pretraining, inference, context window, fine-tuning.

Escribilos en el [glosario C](../glosario/C-como-funcionan-los-llms.md) con ejemplo médico.

## Proyecto

[Extracción de información clínica](../proyectos/03-extraccion-clinica/README.md)

Primero un modelo preentrenado. Después prompts y modelos distintos. El objetivo es separar:

- problemas de **recuperación** (no estaba en el contexto);
- problemas de **generación** (estaba y lo escribió mal);
- problemas del **modelo** (no entiende el dominio).
