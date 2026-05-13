from load_data import load_ab_test_data
from statsmodels.stats.proportion import proportions_ztest


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

# H0: observed conversion difference is due to random chance
# H1: conversion difference is statistically significant

# z-test
z_stat, p_value = proportions_ztest(
    count=[conversions_A, conversions_B], nobs=[users_A, users_B]
)

alpha = 0.05
if p_value < alpha:
    print("Difference statistically significant")
else:
    print("Insufficient evidence of real effect")

# Revenue sanity check
print("\nRevenue metrics by group (mean revenue = ARPU):")
print(
    (
        df.groupby("group")["revenue"].agg(
            ["sum", "mean", "median", "min", "max", "std"]
        )
    ).round(2)
)
