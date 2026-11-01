# Benchmark de epicrisis — Clinical Document Intelligence

Etapa 5. Proyecto de portfolio principal.

**Problema:** convertir una carpeta de internación extensa en una epicrisis coherente, completa y fiel a las fuentes.

## English summary

Head-to-head benchmark of six epicrisis systems (two commercial APIs, open model, structured prompting, LoRA, RAG+verification). Scores factuality, omissions, temporal errors, structure, cost and latency. The fine-tuned model is not assumed to win.

## Preguntas de investigación

- ¿Qué información se pierde al resumir?
- ¿Qué estrategia reduce afirmaciones no respaldadas?
- ¿Cómo se preserva la cronología?
- ¿Qué modelo necesita menos correcciones humanas?
- ¿Cuándo conviene dividir el procesamiento en etapas?
- ¿Cuánto mejora la calidad al verificar contra las notas?

## Sistemas a comparar

| # | Sistema | Qué aislás |
| --- | --- | --- |
| 1 | Modelo comercial A (API) | techo de calidad pago |
| 2 | Modelo comercial B (API) | no enamorarte de una marca |
| 3 | Modelo abierto, crudo | baseline honesto |
| 4 | Abierto + prompt estructurado | cuánto da el prompt |
| 5 | Abierto + LoRA | cuánto da el ajuste |
| 6 | Ajustado + retrieval + verificación | el sistema completo |

## Rúbrica (cada epicrisis, 0–2 por eje)

- Factualidad (¿está en las notas?)
- Omisiones (¿faltó algo grave: alergia, cirugía, cultivo?)
- Errores temporales (fechas y orden)
- Consistencia estructural (secciones que un médico espera)
- Costo (USD / 1k internaciones)
- Latencia (p50 / p95)

No promedies todo en un único “score de IA”. Un modelo puede ganar estructura y perder fidelidad. Eso es el hallazgo.

## Datos

Notas sintéticas con epicrisis de referencia escrita por vos (o un protocolo fijo). Sin PHI.

## Informe final

Un documento que un director médico y un hiring manager puedan leer. Ese informe es el entregable de la Etapa 7.
