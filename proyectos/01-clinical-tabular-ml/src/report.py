from __future__ import annotations

import json
from datetime import date

from .config import REPORTS_DIR


def write_metrics_json(payload: dict) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "metrics.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def _fmt(row: dict, key: str) -> str:
    value = row[key]
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def write_informe(payload: dict) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    reg = payload["regression"]
    clf = payload["classification"]
    winner = min(reg, key=lambda name: reg[name]["mae"])
    lines = [
        "# Informe — Clinical Tabular ML",
        "",
        f"Fecha: {date.today().isoformat()}",
        "",
        "## Problema",
        "",
        "Estimar días de internación al ingreso (o con datos tempranos) sobre un dataset sintético.",
        "El conjunto de prueba se separó **por paciente** para no mezclar internaciones de la misma persona.",
        "",
        "## Datos",
        "",
        f"- Pacientes: {payload['n_patients']}",
        f"- Internaciones: {payload['n_encounters']}",
        f"- Train / test: {payload['n_train']} / {payload['n_test']}",
        f"- Prevalencia de internación ≥ 7 días: {payload['prevalence']:.1%}",
        "",
        "## Regresión (días de internación)",
        "",
        "| Modelo | MAE | IC 95% MAE | RMSE | R² |",
        "| --- | --- | --- | --- | --- |",
    ]
    for name, row in reg.items():
        lines.append(
            f"| {name} | {_fmt(row, 'mae')} | [{row['mae_ci_low']:.3f}, {row['mae_ci_high']:.3f}] | {_fmt(row, 'rmse')} | {_fmt(row, 'r2')} |"
        )
    lines += [
        "",
        f"**Menor MAE en test:** `{winner}`.",
        "",
        "## Clasificación (internación prolongada)",
        "",
        "| Modelo | Precision | Recall | F1 | ROC-AUC | PR-AUC | Brier |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for name, row in clf.items():
        lines.append(
            "| {name} | {precision} | {recall} | {f1} | {roc_auc} | {pr_auc} | {brier} |".format(
                name=name,
                precision=_fmt(row, "precision"),
                recall=_fmt(row, "recall"),
                f1=_fmt(row, "f1"),
                roc_auc=_fmt(row, "roc_auc"),
                pr_auc=_fmt(row, "pr_auc"),
                brier=_fmt(row, "brier"),
            )
        )
    lines += [
        "",
        "## Qué modelo elegiría y por qué",
        "",
        "Este párrafo lo tenés que reescribir vos. El script solo deja una guía:",
        "",
        f"- El menor MAE en test fue `{winner}`. Compará los IC: si se solapan mucho, la diferencia no alcanza para elegir un modelo más complejo.",
        "- Si Ridge está cerca del ganador, preferilo: se explica en un comité clínico.",
        "- Para comunicar riesgo de internación prolongada, mirá calibración y PR-AUC, no solo ROC-AUC.",
        "- Confirmá que las importancias no dependen de `billing_los_code` ni de `n_notes_during_stay`.",
        "",
        "## Limitaciones",
        "",
        "- Datos sintéticos: las relaciones fueron diseñadas. Un dataset real (MIMIC, UCI diabetes 130) puede cambiar el ranking.",
        "- No hay corte temporal: en un hospital real, entrenarías con internaciones viejas y testearías con las nuevas.",
        "- No hay costos clínicos explícitos (cama vs. alarma) para elegir umbral.",
        "",
        "## Figuras",
        "",
        "- `figures/pred_vs_true.png`",
        "- `figures/roc.png`",
        "- `figures/pr.png`",
        "- `figures/calibration.png`",
        "",
    ]
    (REPORTS_DIR / "INFORME.md").write_text("\n".join(lines), encoding="utf-8")
