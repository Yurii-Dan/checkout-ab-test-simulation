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

# Group balance
print(df["group"].value_counts(normalize=True))

# Actual conversion rate
print("\nActual conversion rate, %:")
print(df.groupby("group")["conversion"].mean() * 100)

# Revenue metrics by group
print("\nRevenue metrics by group (mean revenue = ARPU):")
print(df.groupby("group")["revenue"].agg(["sum", "mean", "count", "min", "max"]))

# Logical validation for conversion_date
print(df[(df["conversion"] == 1) & (df["conversion_date"].isnull())])
print(df[(df["conversion"] == 0) & (df["conversion_date"].notnull())])
