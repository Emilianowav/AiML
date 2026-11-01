# Extracción de información clínica estructurada

Etapa 4. Entrada: notas clínicas sintéticas. Salida: JSON con diagnósticos, medicamentos, procedimientos, eventos y fechas, cada uno con referencia a la fuente.

## English summary

Information extraction from synthetic clinical notes to grounded JSON (diagnoses, meds, procedures, events, dates + source spans). Compare pretrained models and prompts; separate retrieval vs generation vs model failures.

## Por qué sintético

Para publicar el repo. Notas reales de pacientes no entran acá.

## Contrato de salida (borrador)

```json
{
  "diagnoses": [{"text": "ICC descompensada", "source_span": "..."}],
  "medications": [{"text": "furosemida 40 mg", "source_span": "..."}],
  "procedures": [],
  "events": [{"text": "ingreso a UCO", "date": "2026-03-12", "source_span": "..."}],
  "dates": [{"text": "alta", "date": "2026-03-18", "source_span": "..."}]
}
```

Si no hay `source_span`, el campo no se acepta. Eso es un guardrail, no un detalle.

## Experimentos

1. Modelo preentrenado (NER o generativo).
2. Varios prompts (cero-shot, few-shot, JSON schema).
3. Varios modelos (abierto chico vs API).
4. Clasificar cada error: recuperación / generación / modelo.

## Métricas mínimas

- Exactitud de entidades (precision/recall por tipo)
- Tasa de alucinación (afirmación sin span)
- Tasa de omisión (estaba en la nota, no salió)
- JSON válido

Este proyecto alimenta el benchmark de epicrisis: si no sabés extraer, el resumen va a inventar.
