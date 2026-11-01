from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
MODELS_DIR = ROOT / "models"
REPORTS_DIR = ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

SEED = 42
N_PATIENTS = 1800
PROLONGED_STAY_DAYS = 7

TARGET_REGRESSION = "length_of_stay_days"
TARGET_CLASSIFICATION = "prolonged_stay"
GROUP_COL = "patient_id"

USABLE_NUMERIC = [
    "age",
    "bmi",
    "systolic_bp",
    "diastolic_bp",
    "heart_rate",
    "glucose",
    "creatinine",
    "hemoglobin",
    "wbc",
    "n_prev_admissions",
    "n_meds_on_admission",
    "diabetes",
    "hypertension",
    "copd",
    "heart_failure",
    "ckd",
    "cancer",
    "emergency_admission",
]

USABLE_CATEGORICAL = [
    "sex",
    "department",
]

LEAKY_FEATURES = [
    "billing_los_code",
    "n_notes_during_stay",
]
