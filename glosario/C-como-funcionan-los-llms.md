# C. Cómo funcionan los LLMs

Esta sección sirve para dejar de tratarlos como cajas negras.

## LLM

- **Qué significa:** Large Language Model, un modelo entrenado para procesar y generar lenguaje.
- **Qué problema resuelve:** tareas de texto (resumir, extraer, responder) sin programar cada patrón lingüístico.
- **Ejemplo médico:** redactar un borrador de epicrisis a partir de notas de internación.

## Transformer

- **Qué significa:** arquitectura neuronal que modela relaciones entre tokens con atención, sin recorrer la secuencia paso a paso como una RNN clásica.
- **Qué problema resuelve:** capturar dependencias a larga distancia (“al ingreso… al alta, 12 días después”).
- **Ejemplo médico:** relacionar un diagnóstico del día 1 con un medicamento del día 8.

## Self-attention

- **Qué significa:** cada token mira a los demás y decide cuánto peso darles.
- **Qué problema resuelve:** saber qué parte del contexto importa para predecir el siguiente token.
- **Ejemplo médico:** al generar “insulina”, el modelo atiende a “glucemia 280” y no a “alergia a dipirona”.

## Token

- **Qué significa:** unidad de texto que el modelo procesa (subpalabra, palabra o símbolo).
- **Qué problema resuelve:** convertir texto variable en una secuencia numérica de largo manejable.
- **Ejemplo médico:** “paracetamol” puede ser un token o varios, según el tokenizer; eso afecta costos y cortes de contexto.

## Embedding

- **Qué significa:** vector numérico que representa un token, un documento o un paciente.
- **Qué problema resuelve:** poner significado en un espacio donde “cerca” implica similitud.
- **Ejemplo médico:** dos fragmentos del manual del HIS sobre “epicrisis” quedan cerca; uno sobre “facturación” queda lejos.

## Context

- **Qué significa:** información disponible para el modelo en una ejecución (prompt, historial, documentos recuperados).
- **Qué problema resuelve:** condicionar la generación. El modelo no “recuerda” tu hospital a menos que se lo pongas (o se lo entrenes).
- **Ejemplo médico:** pegar la nota de evolución + el instructivo de alta antes de pedir la epicrisis.

## Context window

- **Qué significa:** cantidad máxima de tokens que el modelo puede ver.
- **Qué problema resuelve:** nada: es un límite. Vos resolvés el problema partiendo, resumiendo o recuperando.
- **Ejemplo médico:** una carpeta de internación de 80 páginas no entra; hay que chunkear o resumir por etapas.

## Temperature

- **Qué significa:** parámetro que aplana o agudiza la distribución del próximo token.
- **Qué problema resuelve:** controlar creatividad vs. determinismo.
- **Ejemplo médico:** temperature baja para extraer medicamentos a JSON; más alta solo si estás explorando redacciones, nunca para datos clínicos fácticos.

## Fine-tuning

- **Qué significa:** seguir entrenando un modelo ya preentrenado con ejemplos de tu tarea.
- **Qué problema resuelve:** adaptar formato, vocabulario o dominio sin partir de cero.
- **Ejemplo médico:** LoRA sobre epicrisis de tu estilo institucional.

## Instruction tuning

- **Qué significa:** ajuste para que el modelo siga instrucciones (“extraé, no inventes, devolvé JSON”).
- **Qué problema resuelve:** pasar de “completa el texto” a “obedecé una consigna”.
- **Ejemplo médico:** “si no hay fecha de cirugía, devolvé null, no la infieras”.

## RLHF

- **Qué significa:** técnicas que usan feedback humano para alinear el comportamiento (Reinforcement Learning from Human Feedback).
- **Qué problema resuelve:** preferencias difíciles de escribir como loss: tono, seguridad, negativa a inventar.
- **Ejemplo médico:** preferir “no hay registro de alergias en las notas” antes que inventar “sin alergias”.
