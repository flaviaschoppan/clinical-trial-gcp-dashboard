# ----------------------------------------------------------
# Imports
# ----------------------------------------------------------

# standard library
from datetime import datetime, timedelta

# third-party libraries
import numpy as np
import pandas as pd


# ----------------------------------------------------------
# Synthetic patient data generation
# ----------------------------------------------------------

def generate_patient_data(n_patients=150, seed=42):
    """Generate synthetic participant-level clinical trial data."""

    # ----------------------------
    # Random seed
    # ----------------------------
    np.random.seed(seed)

    # ----------------------------
    # Patient identifiers
    # ----------------------------
    patient_ids = [f"PAT-{1000 + i}" for i in range(n_patients)]

    # ----------------------------
    # Trial sites
    # ----------------------------
    sites = np.random.choice(
        ["Site 01", "Site 02", "Site 03", "Site 04"],
        size=n_patients,
        p=[0.30, 0.30, 0.20, 0.20],
    )

    # ----------------------------
    # Treatment allocation
    # ----------------------------
    treatment_arms = np.random.choice(
        [
            "Investigational Arm (Dose A)",
            "High Dose Arm (Dose B)",
            "Standard of Care / Control",
        ],
        size=n_patients,
        p=[0.40, 0.40, 0.20],
    )

    # ----------------------------
    # Patient status
    # ----------------------------
    patient_status = np.random.choice(
        ["Active", "Completed", "Discontinued"],
        size=n_patients,
        p=[0.70, 0.20, 0.10],
    )

    # ----------------------------
    # Demographics
    # ----------------------------
    ages = np.random.randint(18, 76, size=n_patients)
    genders = np.random.choice(["F", "M"], size=n_patients)

    # ----------------------------
    # Enrollment dates
    # ----------------------------
    enrollment_dates = [
        datetime(2026, 1, 15) + timedelta(days=int(d))
        for d in np.random.randint(0, 120, size=n_patients)
    ]

    # ----------------------------
    # Patient dataset
    # ----------------------------
    df_patients = pd.DataFrame(
        {
            "patient_id": patient_ids,
            "site": sites,
            "treatment_arm": treatment_arms,
            "status": patient_status,
            "age": ages,
            "gender": genders,
            "enrollment_date": enrollment_dates,
        }
    )

    return df_patients
