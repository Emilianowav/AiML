"""Genera internaciones sintéticas con estructura de paciente realista.

El target (días de internación) depende de edad, comorbilidades, urgencia y
servicio. Hay ruido a propósito: un modelo perfecto no existe.

También se guardan dos columnas leaky para el ejercicio de fuga de información.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import DATA_RAW, N_PATIENTS, PROLONGED_STAY_DAYS, SEED


DEPARTMENTS = np.array(
    ["clinica_medica", "cirugia", "cardiologia", "neumonologia", "oncologia"]
)


def generate_encounters(n_patients: int = N_PATIENTS, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows: list[dict] = []
    encounter_id = 1

    for patient_id in range(1, n_patients + 1):
        n_enc = int(rng.integers(1, 4))
        sex = rng.choice(["F", "M"])
        # Cada paciente tiene una edad “base”; las internaciones posteriores envejecen poco.
        age0 = int(np.clip(rng.normal(64, 14), 18, 95))
        diabetes = int(rng.random() < 0.28)
        hypertension = int(rng.random() < 0.45)
        copd = int(rng.random() < 0.12)
        heart_failure = int(rng.random() < 0.14)
        ckd = int(rng.random() < 0.11)
        cancer = int(rng.random() < 0.08)

        for k in range(n_enc):
            age = int(np.clip(age0 + k, 18, 96))
            department = rng.choice(DEPARTMENTS, p=[0.38, 0.22, 0.16, 0.12, 0.12])
            emergency = int(rng.random() < 0.41)
            bmi = float(np.clip(rng.normal(27, 5), 16, 48))
            systolic = float(np.clip(rng.normal(128 + 8 * hypertension, 16), 85, 210))
            diastolic = float(np.clip(rng.normal(78 + 5 * hypertension, 10), 50, 120))
            heart_rate = float(np.clip(rng.normal(78 + 6 * copd, 12), 45, 140))
            glucose = float(np.clip(rng.normal(110 + 40 * diabetes, 25), 60, 380))
            creatinine = float(np.clip(rng.normal(0.95 + 0.7 * ckd, 0.35), 0.4, 6.5))
            hemoglobin = float(np.clip(rng.normal(13.2 - 1.2 * cancer, 1.4), 7.0, 17.5))
            wbc = float(np.clip(rng.normal(8.2, 2.4), 3.0, 22.0))
            n_prev = k + int(rng.integers(0, 3))
            n_meds = int(np.clip(rng.normal(4 + 2 * diabetes + 2 * heart_failure, 2), 0, 18))

            los = (
                3.4
                + 0.035 * (age - 55)
                + 1.8 * heart_failure
                + 1.3 * ckd
                + 1.1 * copd
                + 1.6 * cancer
                + 1.4 * emergency
                + 2.2 * (department == "cirugia")
                + 1.5 * (department == "oncologia")
                + 0.08 * n_meds
                + 0.25 * n_prev
                + rng.normal(0, 1.15)
            )
            los = float(np.clip(los, 1.0, 28.0))

            # Leak: se “conoce” la estadía al alta, no al ingreso.
            billing = int(np.clip(np.round(los * 10 + rng.normal(0, 3)), 8, 300))
            n_notes = int(np.clip(np.round(2 + 1.1 * los + rng.normal(0, 1)), 1, 50))

            rows.append(
                {
                    "patient_id": patient_id,
                    "encounter_id": encounter_id,
                    "sex": sex,
                    "age": age,
                    "bmi": round(bmi, 1),
                    "systolic_bp": round(systolic, 0),
                    "diastolic_bp": round(diastolic, 0),
                    "heart_rate": round(heart_rate, 0),
                    "glucose": round(glucose, 0),
                    "creatinine": round(creatinine, 2),
                    "hemoglobin": round(hemoglobin, 1),
                    "wbc": round(wbc, 1),
                    "diabetes": diabetes,
                    "hypertension": hypertension,
                    "copd": copd,
                    "heart_failure": heart_failure,
                    "ckd": ckd,
                    "cancer": cancer,
                    "department": department,
                    "emergency_admission": emergency,
                    "n_prev_admissions": n_prev,
                    "n_meds_on_admission": n_meds,
                    "billing_los_code": billing,
                    "n_notes_during_stay": n_notes,
                    "length_of_stay_days": round(los, 2),
                    "prolonged_stay": int(los >= PROLONGED_STAY_DAYS),
                }
            )
            encounter_id += 1

    return pd.DataFrame(rows)


def save_raw_dataset(path=None) -> pd.DataFrame:
    DATA_RAW.mkdir(parents=True, exist_ok=True)
    df = generate_encounters()
    out = path or (DATA_RAW / "encounters.csv")
    df.to_csv(out, index=False)
    return df


if __name__ == "__main__":
    frame = save_raw_dataset()
    print(f"Filas: {len(frame)}  Pacientes: {frame['patient_id'].nunique()}")
    print(frame["length_of_stay_days"].describe().round(2))
    print("Prolongadas:", frame["prolonged_stay"].mean().round(3))
