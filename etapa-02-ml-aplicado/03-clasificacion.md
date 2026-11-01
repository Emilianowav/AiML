# Regresión logística y clasificación

## Idea

A veces no querés el número de días, querés una decisión: *¿esta internación va a ser prolongada?* Eso es clasificación binaria.

La regresión logística no clasifica “de una”. Estima una **probabilidad**. El umbral 0.5 es una convención, no una ley. En un hospital podés bajar el umbral para no perder internaciones largas (más recall, menos precision).

## Encoding

Sexo, servicio, tipo de admisión son categorías. One-hot (o target encoding con cuidado) las vuelve números. Nunca las pases como 0,1,2,3 a un modelo lineal como si 3 > 2 significara “más servicio”.

## Importancia de variables

En logística, el signo y el tamaño de los coeficientes (en features escaladas) cuentan una historia. En árboles, la importancia es otra: cuánto reduce el error un split.

Si una variable “importante” es `notas_durante_la_estadia`, sospechá leakage.

## Relación con Zoomcamp

El módulo 3 predice churn. Acá: internación ≥ 7 días. Misma matemática, distinto costo del error: un falso negativo puede ser una cama no planificada.

## Tarea

En el informe, respondé: ¿preferís pecar por exceso o por defecto al marcar internaciones prolongadas? Eso define el umbral, no el modelo.
