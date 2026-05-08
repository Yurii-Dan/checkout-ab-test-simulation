# Simulates user-level A/B experiment data
# for a checkout flow optimization test

import random
from datetime import datetime, timedelta
import csv
import os

# Experiment time window
start_date = datetime(2026, 5, 1)
end_date = datetime(2026, 6, 10)

conversion_values = [0, 1]
groups = ["A", "B"]
data = []

for i in range(1, 10001):
    conversion_date = None
    revenue = 0
    user_id = i
    group = random.choices((groups), weights=[0.5, 0.5])[0]
    signup_date = start_date + timedelta(
        days=random.randint(0, (end_date - start_date).days)
    )
    if group == "A":
        conversion = random.choices((conversion_values), weights=[0.95, 0.05])[0]
    else:
        conversion = random.choices((conversion_values), weights=[0.93, 0.07])[0]
    if conversion == 1:
        conversion_date = signup_date + timedelta(days=random.randint(1, 4))
        revenue = random.randint(20, 500)
    data.append([user_id, group, signup_date, conversion, conversion_date, revenue])

# Build correct path to /data folder
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
file_path = os.path.join(base_path, "data", "ab_test_data.csv")

# Export simulated experiment data
with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(
        ["user_id", "group", "signup_date", "conversion", "conversion_date", "revenue"]
    )

    # Write data
    writer.writerows(data)
