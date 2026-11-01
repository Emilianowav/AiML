# Etapa 3 — Deep Learning y PyTorch

Semanas 17–24. Objetivo: entender cómo se entrenan las redes que están detrás de buena parte de la IA moderna.

## Curso

- [Deep Learning Specialization](https://www.deeplearning.ai/courses/deep-learning-specialization/) (redes, optimización, CNN, secuencias, atención, Transformers).
- [Tutoriales oficiales de PyTorch](https://pytorch.org/tutorials/).

## Lo que tiene que quedarte claro

Una red neuronal no es una colección de reglas. Definís una arquitectura, le das ejemplos y una función de pérdida; el entrenamiento ajusta millones de parámetros para reducir esa pérdida.

## Checklist conceptual

- [ ] Neurona, capa, pesos, bias
- [ ] Función de activación
- [ ] Backpropagation y gradiente
- [ ] Loop de entrenamiento
- [ ] Optimizador
- [ ] Embeddings
- [ ] Overfitting y cómo controlarlo
- [ ] Uso de GPU (aunque sea Colab)

## Proyecto

[Redes en PyTorch](../proyectos/02-pytorch-redes/README.md)

Tenés que escribir a mano Dataset, DataLoader, arquitectura, loss, optimizador, loop de train, loop de val, guardado y carga. `model.fit()` no cuenta.
