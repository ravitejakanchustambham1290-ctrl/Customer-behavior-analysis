import pandas as pd

from customer_analytics.transform import clean_customer_data


def sample_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Customer ID": [1, 2, 3],
            "Age": [20, 40, 70],
            "Gender": ["Male", "Female", "Female"],
            "Item Purchased": ["Blouse", "Jeans", "Coat"],
            "Category": ["Clothing", "Clothing", "Outerwear"],
            "Purchase Amount (USD)": [50, 60, 80],
            "Location": ["A", "B", "C"],
            "Size": ["M", "L", "S"],
            "Color": ["Blue", "Red", "Black"],
            "Season": ["Winter", "Summer", "Fall"],
            "Review Rating": [4.0, None, 3.0],
            "Subscription Status": ["Yes", "No", "No"],
            "Shipping Type": ["Express", "Standard", "Standard"],
            "Discount Applied": ["Yes", "No", "No"],
            "Promo Code Used": ["Yes", "No", "No"],
            "Previous Purchases": [1, 5, 12],
            "Payment Method": ["Cash", "Card", "PayPal"],
            "Frequency of Purchases": ["Weekly", "Monthly", "Annually"],
        }
    )


def test_cleaning_pipeline_creates_expected_features_and_schema():
    cleaned = clean_customer_data(sample_data())

    assert "purchase_amount" in cleaned.columns
    assert "age_group" in cleaned.columns
    assert "purchase_frequency_days" in cleaned.columns
    assert "promo_code_used" not in cleaned.columns
    assert cleaned["review_rating"].isna().sum() == 0
    assert cleaned["purchase_frequency_days"].tolist() == [7, 30, 365]


def test_age_groups_are_ordered_categoricals():
    cleaned = clean_customer_data(sample_data())
    assert list(cleaned["age_group"].cat.categories) == [
        "young adult",
        "adult",
        "middle age",
        "senior",
    ]
