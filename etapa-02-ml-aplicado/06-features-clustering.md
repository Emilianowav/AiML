# Features, clustering, dimensionalidad y leakage

Estos temas están en tu programa aunque Zoomcamp los reparte entre módulos.

## Feature engineering

Crear variables que el modelo pueda usar: edad en bins, recuento de comorbilidades, “es urgencia”, logs de laboratorio. No es magia; es traducir conocimiento clínico a columnas.

## Selección de variables

Sacar ruido. Un modelo con 8 variables estables le gana, en la práctica, a uno con 200 columnas copiadas del HIS.

## Clustering y reducción de dimensionalidad

No predicen días por sí solos. Sirven para:

- agrupar pacientes parecidos (estratificar errores);
- comprimir laboratorios correlacionados (PCA);
- diagnosticar si hay subpoblaciones donde el modelo falla (cirugía vs clínica).

## Data leakage

Fuga de información: el modelo ve algo que no tendría en el momento de predecir.

Ejemplos en internación:

- código de facturación que se carga al alta;
- cantidad de notas *durante* toda la estadía, si predecís al ingreso;
- el propio `length_of_stay` disfrazado;
- mezclar las 4 internaciones de Ana entre train y test.

El dataset sintético incluye columnas leaky a propósito. El pipeline las excluye. El ejercicio es dejarlas entrar una vez y ver cómo “mejora” el MAE. Esa mejora es falsa.

## Interpretabilidad

Coeficientes, importancias, errores por grupo de edad o servicio. Un clínico tiene derecho a preguntar por qué.

## Desbalance

Internación prolongada es minoritaria. Accuracy no alcanza; usá PR-AUC, F1 y un umbral elegido en validación, no en test.
