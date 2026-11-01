# B. Cómo aprende un modelo

Estos términos aparecen en Zoomcamp, en Andrew Ng y en cualquier entrevista de ML.

## Parámetros

- **Qué significa:** valores internos que el modelo ajusta durante el entrenamiento (coeficientes, pesos, umbrales de un árbol).
- **Qué problema resuelve:** almacenar lo aprendido.
- **Ejemplo médico:** en una regresión lineal, el coeficiente de `heart_failure` dice cuántos días extra de internación asocia el modelo a esa comorbilidad.

## Hiperparámetros

- **Qué significa:** decisiones que configurás vos: learning rate, profundidad del árbol, `n_estimators`, batch size.
- **Qué problema resuelve:** controlar capacidad y velocidad de aprendizaje. No se “aprenden” solos en el entrenamiento básico; se eligen y se validan.
- **Ejemplo médico:** un Random Forest con árboles profundos puede memorizar pacientes del hospital A y fallar en el B.

## Epoch

- **Qué significa:** una pasada completa por los datos de entrenamiento.
- **Qué problema resuelve:** dar al modelo varias oportunidades de ver cada ejemplo.
- **Ejemplo médico:** en PyTorch, 20 epochs sobre notas clínicas; si el loss de validación sube, parás (early stopping).

## Batch

- **Qué significa:** un grupo de ejemplos procesados juntos.
- **Qué problema resuelve:** estimar el gradiente sin usar todo el dataset en cada paso, y aprovechar la GPU.
- **Ejemplo médico:** 32 internaciones por batch al entrenar una red tabular.

## Learning rate

- **Qué significa:** tamaño del paso al actualizar parámetros.
- **Qué problema resuelve:** equilibrar velocidad y estabilidad. Muy grande: el loss explota. Muy chico: no termina nunca.
- **Ejemplo médico:** al fine-tunear un LLM con LoRA, un learning rate agresivo puede destruir el lenguaje clínico que el modelo ya tenía.

## Backpropagation

- **Qué significa:** cálculo de cuánto contribuyó cada parámetro al error, de atrás hacia adelante.
- **Qué problema resuelve:** saber en qué dirección mover los pesos.
- **Ejemplo médico:** si el modelo se equivoca en “alta a las 48 h”, backprop reparte esa culpa entre capas que leyeron la nota de guardia.

## Optimizer

- **Qué significa:** algoritmo que usa los gradientes para actualizar parámetros (SGD, Adam, AdamW).
- **Qué problema resuelve:** no actualizar “a ojo”.
- **Ejemplo médico:** AdamW en el entrenamiento de la red de clasificación de notas.

## Regularization

- **Qué significa:** técnicas para evitar que el modelo memorice (L2, dropout, early stopping, menos features).
- **Qué problema resuelve:** overfitting.
- **Ejemplo médico:** Ridge en duración de internación penaliza coeficientes enormes de una variable rara (“código de cama 12B”).

## Validation

- **Qué significa:** evaluación durante el desarrollo para tomar decisiones (qué modelo, qué umbral, qué features).
- **Qué problema resuelve:** elegir sin mirar el test.
- **Ejemplo médico:** GroupKFold por `patient_id` para decidir entre Forest y XGBoost.

## Test set

- **Qué significa:** datos reservados para la evaluación final, tocados una vez.
- **Qué problema resuelve:** estimar el desempeño real.
- **Ejemplo médico:** pacientes que nunca aparecieron en train ni en validación. Si un paciente tiene 3 internaciones, las 3 van juntas.
