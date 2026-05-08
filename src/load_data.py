import pandas as pd
import os

"""
Load and preprocess A/B test dataset.
"""


def load_ab_test_data():

    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "..", "data", "ab_test_data.csv")

    df = pd.read_csv(data_path)

    # Convert columns to appropriate data types
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    df["conversion_date"] = pd.to_datetime(df["conversion_date"])
    df["group"] = df["group"].astype("category")

    return df


if __name__ == "__main__":
    df = load_ab_test_data()
    print(df.head())
