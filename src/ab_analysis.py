from load_data import load_ab_test_data
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import ttest_ind


# Load prepared dataset
df = load_ab_test_data()

# Number of users in each group
users_A = len(df[df["group"] == "A"])
print(f"Users in group A: {users_A}")
users_B = len(df[df["group"] == "B"])
print(f"Users in group B: {users_B}")

# Number of conversions in each group
conversions_A = len(df[(df["group"] == "A") & (df["conversion"] == 1)])
print(f"Conversions in group A: {conversions_A}")
conversions_B = len(df[(df["group"] == "B") & (df["conversion"] == 1)])
print(f"Conversions in group B: {conversions_B}")

# Conversion Rate in each group
conversion_rate_A = round(conversions_A / users_A * 100, 2)
conversion_rate_B = round(conversions_B / users_B * 100, 2)
print(f"Conversion rate in group A: {conversion_rate_A}%")
print(f"Conversion rate in group B: {conversion_rate_B}%")

# H0: observed conversion difference is due to random chance
# H1: conversion difference is statistically significant

# z-test
print("\n--- Conversion Analysis ---")
z_stat, p_value = proportions_ztest(
    count=[conversions_A, conversions_B], nobs=[users_A, users_B]
)
print(f"Conversion P-value: {p_value:.2e}")
alpha = 0.05
if p_value < alpha:
    print("Conversion difference is statistically significant")
else:
    print("Insufficient evidence of real effect for conversion")

# Revenue sanity check
print("\nRevenue metrics by group (mean revenue = ARPU):")
print(
    (
        df.groupby("group")["revenue"].agg(
            ["sum", "mean", "median", "min", "max", "std"]
        )
    ).round(2)
)

# All revenue values in each group
group_A = df[df["group"] == "A"]
revenue_A = group_A["revenue"]
group_B = df[df["group"] == "B"]
revenue_B = group_B["revenue"]

# t-test
print("\n--- Revenue Analysis ---")
t_stat, p_value = ttest_ind(revenue_A, revenue_B, equal_var=False)
print(f"Revenue P-value: {p_value:.2e}")
if p_value < alpha:
    print("ARPU difference is statistically significant")
else:
    print("The difference is not statistically significant for ARPU")
