import pandas as pd

from load_data import load_ab_test_data


# Load prepared dataset
df = load_ab_test_data()

# --------------------------------------------------------------------
# BASIC EDA
# --------------------------------------------------------------------

# Display first 5 rows of the dataset
print("\nFirst rows of dataset:")
print(df.head())

# Show dataset structure and column types
print("\nDataset info:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# -------------------------------------------------------------------
# ANALYSIS
# -------------------------------------------------------------------

# Group balance
print(df["group"].value_counts(normalize=True))

# Actual conversion rate
print(df.groupby("group")["conversion"].sum()) 
