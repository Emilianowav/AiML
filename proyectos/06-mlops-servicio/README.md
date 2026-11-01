# Servicio MLOps

Etapa 6. Convertir Clinical Tabular ML en un servicio desplegable.

```text
Dataset → Preprocessing → Training → Evaluation
       → Model Registry → FastAPI → Application → Monitoring
```

## English summary

Packages the length-of-stay model as a versioned FastAPI service with Docker, experiment tracking and basic monitoring. A request returns the prediction plus model version for reproducibility.

## Contrato del endpoint

```json
POST /predict
{
  "patient_features": { "age": 74, "heart_failure": 1, "emergency_admission": 1 }
}

200
{
  "length_of_stay_days": 7.2,
  "model_name": "xgboost",
  "model_version": "2026.11.01+abc123",
  "trained_at": "2026-11-01T12:00:00Z"
}
```

Sin versión en la respuesta, no es reproducible.

## Checklist

- [ ] MLflow (o equivalente) registra params, métricas y artefacto
- [ ] FastAPI lee el modelo del registry, no un path mágico
- [ ] Docker build + run local
- [ ] GitHub Actions: tests + lint
- [ ] Evidently: reporte de drift sobre un batch de internaciones nuevas
- [ ] README con `docker compose up` y un `curl` de ejemplo

## Qué no hace falta al principio

Kubernetes completo. Primero un contenedor que predice bien y deja rastro. K8s entra si el Zoomcamp de MLOps lo pide, no como adorno.
