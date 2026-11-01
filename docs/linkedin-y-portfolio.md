# LinkedIn, GitHub y búsqueda laboral

Este repo está pensado para mostrarse. Eso impone un criterio: cada carpeta de `proyectos/` tiene que poder entenderla alguien que no cursó con vos.

## Qué mostrar (y qué no)

**Mostrar**

- El README del proyecto: problema, datos, método, resultado, decisión.
- Gráficos de evaluación (ROC, calibración, errores por grupo).
- El motivo por el que **no** elegiste el modelo con mejor número bruto.
- Código que se puede reproducir con un comando.

**No mostrar**

- Tareas copiadas de un curso.
- Métricas sin intervalo de confianza ni set de prueba.
- Demos con datos reales de pacientes.
- API keys, notebooks sin explicación, o un `.pkl` suelto.

## Cómo hablar de Clinical Tabular ML

Texto corto para GitHub / LinkedIn:

> Entrené modelos para estimar duración de internación sobre datos tabulares clínicos (sintéticos, para poder publicar). Comparé regresión lineal, Random Forest y XGBoost con un corte por paciente para evitar fuga de información. El informe justifica el modelo elegido con MAE, intervalos de confianza e interpretabilidad, no solo con el ranking de accuracy.

## Proyectos que más pesan en una entrevista

1. **Clinical Tabular ML** — demuestra ML clásico bien evaluado.
2. **Benchmark de epicrisis** — demuestra criterio con LLMs, no solo prompting.
3. **Asistente de conocimiento** — demuestra RAG, citas y abstención.
4. **Servicio MLOps** — demuestra que el modelo sale de la notebook.

## Checklist antes de pegar el repo en LinkedIn

- [ ] README raíz en español claro, con tabla de proyectos.
- [ ] Cada proyecto con README propio y resultado reproducible.
- [ ] Sin `.env`, sin PHI, sin notebooks enormes sin ejecutar.
- [ ] Un informe que dice qué elegirías **y por qué**.
- [ ] CV en español e inglés apuntando a 2 o 3 proyectos, no a 20 carpetas.

Plantillas de textos y CV: [`etapa-07-consolidacion`](../etapa-07-consolidacion/README.md).
