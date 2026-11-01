# Etapa 6 — MLOps, despliegue y producción

Semanas 41–48. Entrenar no alcanza: hay que operar.

## Curso

- [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp)
- [Made With ML](https://madewithml.com/)

## Herramientas

MLflow, Docker, FastAPI, Evidently, GitHub Actions, PostgreSQL, GPU en la nube cuando el local no alcance.

## Flujo que tenés que implementar

```text
Dataset → Preprocessing → Training → Evaluation
       → Model Registry → FastAPI → Application → Monitoring
```

## Proyecto

[Servicio MLOps](../proyectos/06-mlops-servicio/README.md)

El servicio recibe una entrada, predice, registra la versión del modelo y devuelve un resultado reproducible. El candidato natural es el modelo de Clinical Tabular ML.
