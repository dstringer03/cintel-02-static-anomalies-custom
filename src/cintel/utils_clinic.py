"""utils_clinic.py.

Author: Darrion Maurice Stringer
Date: 2026-10

Shared helper functions for the clinic anomaly-detection domain.

Used by:
- src/cintel/anomaly_detector.py (cintel-02)
- app.py
"""

from pathlib import Path

import polars as pl


def load_clinic_data(data_file: Path) -> pl.DataFrame:
    """Read pediatric clinic age/height records from a CSV file."""
    return pl.read_csv(data_file)


def detect_clinic_anomalies(
    df: pl.DataFrame,
    max_age_years: float,
    max_height_inches: float,
    min_age_years: float | None = None,
) -> pl.DataFrame:
    """Return records outside the configured screening thresholds."""
    flagged = (pl.col("age_years") >= max_age_years) | (
        pl.col("height_inches") >= max_height_inches
    )

    if min_age_years is not None:
        flagged = flagged | (pl.col("age_years") < min_age_years)

    return df.filter(flagged)
