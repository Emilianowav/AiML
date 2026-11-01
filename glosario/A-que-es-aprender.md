# A. Qué es aprender

Jerarquía didáctica (es una simplificación):

```text
Inteligencia Artificial
  └── Machine Learning
        └── Deep Learning
              └── Transformers y modelos de lenguaje
```

Existen áreas de IA sin Machine Learning, y modelos de Deep Learning que no son Transformers.

## Artificial Intelligence

- **Qué significa:** campo que busca sistemas capaces de hacer tareas asociadas con inteligencia: clasificar, predecir, generar lenguaje, decidir.
- **Qué problema resuelve:** automatizar o asistir trabajo cognitivo que antes exigía una persona.
- **Ejemplo médico:** un módulo que sugiere una epicrisis o responde cómo usar una pantalla del HIS no “es IA” por magia: es un sistema diseñado con datos, modelos y reglas de uso.

## Machine Learning

- **Qué significa:** métodos que aprenden patrones a partir de datos, en lugar de reglas escritas una por una.
- **Qué problema resuelve:** cuando las reglas explotan (“si diabetes y creatinina alta y edad > 80…” se vuelve inmantenible).
- **Ejemplo médico:** estimar días de internación a partir de edad, comorbilidades y tipo de admisión. Eso es el proyecto Clinical Tabular ML.

## Deep Learning

- **Qué significa:** Machine Learning basado en redes neuronales con varias capas.
- **Qué problema resuelve:** representar relaciones complejas (imágenes, texto, señales) que un modelo lineal no captura bien.
- **Ejemplo médico:** una red que lee una nota clínica y extrae medicamentos; el “conocimiento” está en los pesos, no en un `if "ibuprofeno" in texto`.

## Neural Network

- **Qué significa:** modelo compuesto por capas de operaciones matemáticas (multiplicar, sumar, activar).
- **Qué problema resuelve:** aproximar funciones complicadas combinando transformaciones simples.
- **Ejemplo médico:** una capa puede aprender que “HTA” y “hipertensión arterial” están cerca; otra, que esa condición junto a internación de urgencia aumenta el riesgo.

## Training

- **Qué significa:** ajustar los parámetros del modelo para reducir una función de pérdida sobre ejemplos.
- **Qué problema resuelve:** pasar de un modelo inútil (pesos aleatorios o coeficientes vacíos) a uno que predice.
- **Ejemplo médico:** entrenar XGBoost con internaciones históricas sintéticas hasta que el error de días de estadía baje en validación.

## Inference

- **Qué significa:** ejecutar un modelo ya entrenado para obtener una predicción o un texto.
- **Qué problema resuelve:** usar el modelo en producción, sin recalcular todos los pesos.
- **Ejemplo médico:** un médico carga datos de admisión y el servicio devuelve “estadía esperada: 6 días (IC 4–9)”.

## Generalization

- **Qué significa:** funcionar con datos que el modelo no vio en el entrenamiento.
- **Qué problema resuelve:** evitar el espejismo de “en el Excel dio 99%”.
- **Ejemplo médico:** el modelo tiene que servir para pacientes nuevos, no para re-predecir las internaciones con las que se entrenó. Por eso el corte es por paciente, no por fila.
