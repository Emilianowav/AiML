# Introducción: cuándo usar Machine Learning

## Idea

Machine Learning sirve cuando hay un patrón en datos históricos que una persona no puede (o no quiere) escribir como reglas. No sirve cuando el problema es un reglamento explícito, cuando no hay datos, o cuando una predicción errónea es inaceptable y no hay forma de supervisar.

## CRISP-DM, en una internación

1. **Negocio:** ¿para qué queremos la duración de internación? ¿Cama, comunicación a familia, staffing?
2. **Datos:** encuentros, no pacientes sueltos. Un paciente puede internarse varias veces.
3. **Preparación:** missing values, categorías, leakage.
4. **Modelado:** lineal → árboles → boosting.
5. **Evaluación:** error en pacientes nunca vistos.
6. **Despliegue:** más adelante (Etapa 6). Ahora el “despliegue” es un informe reproducible.

## ML vs reglas, ejemplo médico

- Regla: “si hay cirugia mayor, estadía mínima 3 días”. Útil, rígida, fácil de auditar.
- Modelo: combina edad, insuficiencia cardíaca, urgencia y laboratorio. Más flexible, más opaca, necesita evaluación.

En producción suelen convivir: el modelo sugiere, una regla de negocio recorta disparates (“nunca predecir 0 días si hubo cirugía”).

## Supervisado

Tenés X (features al ingreso o durante la internación) e y (días reales al alta). Si usás información que **solo existe al final** de la internación, estás haciendo trampa. Eso es leakage: ver [06-features-clustering.md](06-features-clustering.md).

## Tarea

Escribí en una frase el objetivo del proyecto clínico: qué se predice, cuándo se predice (al ingreso, a las 24 h), y para quién es útil el número.
