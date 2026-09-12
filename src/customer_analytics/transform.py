"""Reusable data-cleaning and feature-engineering functions."""

from __future__ import annotations

import pandas as pd

FREQUENCY_TO_DAYS = {
    "Weekly": 7,
    "Fortnightly": 14,
    "Bi-Weekly": 14,
    "Monthly": 30,
    "Quarterly": 90,
    "Every 3 Months": 90,
    "Annually": 365,
}

AGE_GROUP_LABELS = ["young adult", "adult", "middle age", "senior"]


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with SQL/Python-friendly snake_case column names."""
    result = df.copy()
    result.columns = (
        result.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    )
    return result.rename(columns={"purchase_amount_(usd)": "purchase_amount"})


def impute_review_rating(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing review ratings with the median rating within each category."""
    result = df.copy()
    result["review_rating"] = result.groupby("category")["review_rating"].transform(
        lambda series: series.fillna(series.median())
    )
    return result


def add_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """Create four equal-frequency age groups from the age distribution."""
    result = df.copy()
    result["age_group"] = pd.qcut(
        result["age"], q=4, labels=AGE_GROUP_LABELS
    )
    return result


def add_purchase_frequency_days(df: pd.DataFrame) -> pd.DataFrame:
    """Convert purchase-frequency labels into approximate days between purchases."""
    result = df.copy()
    result["purchase_frequency_days"] = result["frequency_of_purchases"].map(
        FREQUENCY_TO_DAYS
    )
    return result


def remove_redundant_promo_column(df: pd.DataFrame) -> pd.DataFrame:
    """Remove promo_code_used after confirming it duplicates discount_applied."""
    result = df.copy()
    if "promo_code_used" in result.columns and "discount_applied" in result.columns:
        if not (result["promo_code_used"] == result["discount_applied"]).all():
            raise ValueError("promo_code_used and discount_applied are not identical")
        result = result.drop(columns=["promo_code_used"])
    return result


def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """Run the complete, deterministic customer-data preparation pipeline."""
    result = standardize_columns(df)
    result = impute_review_rating(result)
    result = add_age_group(result)
    result = add_purchase_frequency_days(result)
    result = remove_redundant_promo_column(result)
    return result
