# D. Cómo se construyen aplicaciones con LLMs

Acá aparece lo que ya viene del trabajo con módulos reales: soporte y documentos clínicos.

## Prompt engineering

- **Qué significa:** diseñar instrucciones, ejemplos y contexto para una tarea.
- **Qué problema resuelve:** sacar más de un modelo sin entrenarlo.
- **Ejemplo médico:** un prompt que exige JSON con diagnósticos, medicamentos y `source_span`.

## Tool calling

- **Qué significa:** el modelo pide ejecutar una herramienta (buscar, calcular, consultar una API) y usa el resultado.
- **Qué problema resuelve:** no fingir que el LLM “tiene” la base de pacientes o la versión del manual.
- **Ejemplo médico:** llamar a un retriever del manual del HIS antes de explicar cómo generar una epicrisis.

## RAG

- **Qué significa:** Retrieval-Augmented Generation: recuperar información externa y usarla para responder.
- **Qué problema resuelve:** alucinar sobre un sistema que cambia, o sobre una internación que el modelo no vio.
- **Ejemplo médico:** el asistente funcional recupera el capítulo del manual y recién después redacta. Que el manual se haya escrito con IA no lo vuelve verdadero: también necesita revisión.

## Chunking

- **Qué significa:** partir documentos en fragmentos.
- **Qué problema resuelve:** entrar en el context window y recuperar pasajes precisos.
- **Ejemplo médico:** cortar el manual por pantalla/sección, no cada 500 caracteres a mitad de una tabla.

## Retrieval

- **Qué significa:** buscar los fragmentos más relevantes para una pregunta.
- **Qué problema resuelve:** no mandarle 400 páginas al modelo.
- **Ejemplo médico:** pregunta “¿cómo anulo un estudio?” → recupera la sección de anulación, no la de instalación.

## Reranking

- **Qué significa:** reordenar lo recuperado con un modelo más preciso (y más caro).
- **Qué problema resuelve:** el primer retriever es rápido y tosco; el reranker corrige.
- **Ejemplo médico:** de 20 chunks sobre “estudio”, dejar 3 que hablan de anulación ambulatoria.

## Agent

- **Qué significa:** sistema que usa un modelo para decidir pasos, herramientas o acciones.
- **Qué problema resuelve:** tareas de varios saltos (“buscá, verificá, preguntá si falta dato”).
- **Ejemplo médico:** un agente de epicrisis que primero lista documentos, después extrae eventos, después redacta, después verifica citas.

## Orchestration

- **Qué significa:** coordinación entre modelos, herramientas y procesos.
- **Qué problema resuelve:** que no sea un único prompt gigante e inmanejable.
- **Ejemplo médico:** pipeline: OCR/notas → extracción → línea de tiempo → redacción → verificación.

## Guardrails

- **Qué significa:** restricciones y validaciones para limitar comportamientos indeseados.
- **Qué problema resuelve:** JSON inválido, diagnósticos inventados, consejos peligrosos, filtrado de PHI.
- **Ejemplo médico:** si el modelo afirma un procedimiento sin `source_span`, se rechaza el campo.

## Evaluation

- **Qué significa:** medir calidad de forma sistemática, no “a mí me gustó”.
- **Qué problema resuelve:** saber si un prompt nuevo mejoró factualidad o solo el estilo.
- **Ejemplo médico:** benchmark de 50 epicrisis sintéticas con scores de omisión, error temporal y costo.
