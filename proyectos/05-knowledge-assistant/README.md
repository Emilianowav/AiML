# Asistente de conocimiento funcional

Etapas 4–5. Complemento del benchmark de epicrisis.

**Problema:** responder preguntas de usuarios sobre un sistema de software complejo usando su documentación.

La epicrisis es generación y síntesis. Este proyecto es **recuperación y fundamentación**. Juntos cubren LLM Engineering de verdad.

## English summary

RAG assistant over a software manual: measure retrieval, grounded answers, citations and correct abstention when the docs are missing or contradictory.

## Preguntas de investigación

- ¿Qué fragmentos recupera el sistema?
- ¿La respuesta está respaldada por la documentación?
- ¿Qué pasa si el manual es ambiguo o contradictorio?
- ¿Puede reconocer cuándo no sabe?
- ¿Qué impacto tienen chunking y reranking?
- ¿Cómo se sincroniza el índice cuando sale una versión nueva del producto?

## Métricas

- Recall@k del retrieval (¿el chunk correcto estaba entre los k?)
- Precisión de la respuesta (juzgada con rúbrica, no con “se siente bien”)
- Citas: ¿el span existe en el manual?
- Tasa de abstención correcta (dijo “no está documentado” cuando no estaba)
- Tasa de abstención incorrecta (se calló y sí estaba)

## Diseño mínimo

```text
pregunta → embed → retrieve → (rerank) → prompt con citas → JSON
                                              ↓
                                    guardrail: cada claim cita un chunk
```

Usá un recorte de manual (el de tu HIS, sanitizado, o un manual público de un HIS de código abierto). Versioná el corpus: v1 vs v2 es parte del experimento.
