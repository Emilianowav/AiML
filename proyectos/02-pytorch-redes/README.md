# Redes neuronales en PyTorch

Etapa 3. Dos redes escritas a mano: una de clasificación (p. ej. imágenes o texto corto) y otra tabular (internación).

## English summary

Two from-scratch PyTorch training loops (classification + tabular). Dataset, DataLoader, architecture, loss, optimizer, train/val loops, save/load. No `model.fit()`.

## Restricción

Si importás una arquitectura lista y llamás `fit`, el proyecto no cumple. El valor está en el loop.

## Checklist de código

- [ ] `Dataset` y `DataLoader`
- [ ] Arquitectura (`nn.Module`)
- [ ] Función de pérdida
- [ ] Optimizador
- [ ] Loop de entrenamiento
- [ ] Loop de validación
- [ ] Guardado y carga (`state_dict`)
- [ ] Curva de loss train vs val (overfitting visible)

## Idea tabular

Reutilizar el CSV de Clinical Tabular ML. Una MLP chica no tiene que ganarle a XGBoost. Tiene que ser *correcta*: split por paciente, early stopping, y un MAE comparable, no milagroso.

## Idea de clasificación

Empezá simple (Fashion-MNIST o un CSV de diagnóstico binario). Después, si querés, una CNN chica.

Cuando esté listo, este README pasa a mostrar métricas y un párrafo de por qué la red perdió o ganó contra el modelo tabular clásico.
