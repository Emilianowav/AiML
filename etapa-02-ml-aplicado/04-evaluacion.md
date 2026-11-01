# Evaluación: los números que no podés ignorar

Accuracy miente cuando hay desbalance. Si solo el 18% de las internaciones son prolongadas, un modelo que siempre dice “no” acierta el 82% y no sirve.

| Métrica | Pregunta que responde | Cuándo mirarla |
| --- | --- | --- |
| Precision | De las que marqué positivas, ¿cuántas lo eran? | Cuando el falso positivo es caro (alarma al staff) |
| Recall | De las positivas reales, ¿cuántas vi? | Cuando el falso negativo es caro (no preparar una cama larga) |
| F1 | ¿Hay un equilibrio razonable? | Cuando no podés optimizar solo una |
| ROC-AUC | ¿El modelo ordena bien riesgo vs no riesgo? | Comparar modelos; no elige umbral |
| PR-AUC | ¿Ese orden se sostiene con pocos positivos? | Desbalance |
| Calibration | Si digo 30%, ¿pasa ~30% de las veces? | Cuando vas a mostrar una probabilidad a un clínico |
| IC | ¿El 0.81 de AUC es estable o un golpe de suerte? | Siempre, en el informe final |

## Validación cruzada

Un solo split puede ser generoso o cruel. GroupKFold por paciente repite el experimento sin romper el principio de no-fuga.

## Relación con Zoomcamp

El módulo 4 suele ser el más difícil. Hacé las métricas a mano en `ejercicios/metricas_desde_cero.py` hasta que la matriz de confusión te salga sin mirar Wikipedia.

## Tarea

Mirar la curva de calibración del proyecto. Si el modelo dice 0.7 y en realidad ocurre 0.4, no lo uses para comunicar riesgo.
