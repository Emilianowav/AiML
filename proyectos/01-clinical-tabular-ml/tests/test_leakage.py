from src.dataset import assert_no_patient_overlap, split_by_patient
from src.generate_data import generate_encounters


def test_no_patient_overlap():
    df = generate_encounters(n_patients=200, seed=0)
    train, test = split_by_patient(df, seed=0)
    assert_no_patient_overlap(train, test)
    assert set(train["patient_id"]).isdisjoint(set(test["patient_id"]))


def test_same_patient_stays_together():
    df = generate_encounters(n_patients=200, seed=1)
    train, test = split_by_patient(df, seed=1)
    for patient in df["patient_id"].unique():
        in_train = (train["patient_id"] == patient).any()
        in_test = (test["patient_id"] == patient).any()
        assert in_train + in_test == 1


def test_leaky_columns_exist_but_are_optional():
    df = generate_encounters(n_patients=50, seed=2)
    assert "billing_los_code" in df.columns
    assert "n_notes_during_stay" in df.columns
    # Correlación alta con el target: si las usás, estás haciendo trampa.
    corr = df["billing_los_code"].corr(df["length_of_stay_days"])
    assert corr > 0.9
