# ==============================================================================
# 📝 PRACTICE.py — Phase 3: Practice Set 2
# Topic: Advanced Indexing & Selection — .loc vs .iloc & Safe Conditional Filtering
# ==============================================================================
# Instructions:
# Write your code directly under each problem where marked.
# Do not delete or overwrite the problem setup code.
# When you have completed all problems, save this file and say: "check it"!
# ==============================================================================
import pandas as pd
import numpy as np

# ------------------------------------------------------------------------------
# Problem 1: Label-Based Selection with .loc (Inclusive Slicing)
# ------------------------------------------------------------------------------
# A hospital manages patient triage records indexed by unique Patient ID:
patients_data = {
    "name": ["John", "Sarah", "Mike", "Emma", "David"],
    "age": [45, 29, 62, 38, 51],
    "blood_pressure": [140, 118, 155, 122, 130],
    "department": ["Cardio", "General", "Cardio", "Orthopedic", "General"]
}
df_patients = pd.DataFrame(patients_data, index=["P101", "P102", "P103", "P104", "P105"])

# Task:
# 1. Using `.loc`, extract the entire record for patient "P103" as a Series.
#    Store in `patient_p103`.
# 2. Using `.loc`, extract the blood pressure for patient "P102" (scalar value).
#    Store in `bp_p102`.
# 3. Using `.loc`, slice patients from "P102" through "P104" (inclusive!)
#    and extract only the "name" and "department" columns.
#    Store this sub-DataFrame in `triage_subset`.

# Write your code for Problem 1 below:




# ------------------------------------------------------------------------------
# Problem 2: Positional Selection with .iloc (Exclusive Offset Slicing)
# ------------------------------------------------------------------------------
# In algorithmic trading, server latency and price ticks arrive in time order.
# The table uses arbitrary or non-numeric index labels:
market_data = {
    "timestamp": ["09:30:00", "09:30:01", "09:30:02", "09:30:03", "09:30:04"],
    "ticker": ["AAPL", "AAPL", "AAPL", "GOOG", "GOOG"],
    "price": [182.50, 182.75, 182.40, 175.20, 175.90],
    "volume": [500, 1200, 300, 800, 1500]
}
df_market = pd.DataFrame(market_data, index=["tick_a", "tick_b", "tick_c", "tick_d", "tick_e"])

# Task:
# 1. Using `.iloc`, extract the first 3 rows (rows 0, 1, 2) and the first 2 columns (0, 1).
#    Remember: `.iloc` follows standard Python half-open interval rules [start:stop)!
#    Store in `top_ticks`.
# 2. Using `.iloc`, extract the very last row as a Series (use negative indexing -1).
#    Store in `latest_tick`.
# 3. Using `.iloc`, extract rows at indices 1 and 3, and columns at indices 2 and 3 ("price" & "volume").
#    Store in `sampled_market`.

# Write your code for Problem 2 below:




# ------------------------------------------------------------------------------
# Problem 3: Multi-Condition Boolean Filtering on DataFrames
# ------------------------------------------------------------------------------
# In HR analytics, we filter employee records based on performance and tenure:
hr_data = {
    "emp_id": [201, 202, 203, 204, 205, 206],
    "name": ["Alex", "Brian", "Catherine", "Daniel", "Eva", "Frank"],
    "department": ["Engineering", "Sales", "Engineering", "Marketing", "Engineering", "Sales"],
    "salary": [95000, 72000, 115000, 68000, 105000, 88000],
    "rating": [4.8, 3.5, 4.9, 4.1, 3.9, 4.6]
}
df_hr = pd.DataFrame(hr_data).set_index("emp_id")

# Task:
# 1. Filter `df_hr` to find all employees where:
#    - "department" is "Engineering" AND
#    - "rating" is strictly greater than 4.0
#    (Remember to use `&` and wrap each condition in parentheses!).
#    Store the filtered DataFrame in `top_engineers`.
# 2. Filter `df_hr` to find all employees where:
#    - "salary" is greater than or equal to 100000 OR
#    - "rating" is greater than or equal to 4.5
#    (Use `|` with parentheses).
#    Store in `high_performers_or_earners`.

# Write your code for Problem 3 below:




# ------------------------------------------------------------------------------
# Problem 4: Safe In-Place Modification (Avoiding SettingWithCopyWarning)
# ------------------------------------------------------------------------------
# In customer churn prevention, telecom companies award loyalty bonus minutes
# to accounts flagged as at-risk.
churn_data = {
    "account_id": [501, 502, 503, 504],
    "monthly_charges": [85.0, 45.0, 95.0, 60.0],
    "contract_months": [2, 24, 1, 12],
    "loyalty_bonus": [0, 0, 0, 0]
}
df_telecom = pd.DataFrame(churn_data).set_index("account_id")

# Task:
# 1. At-risk condition: An account is at risk if "contract_months" <= 3 AND "monthly_charges" > 70.0.
#    Using `.loc[condition, "loyalty_bonus"] = 500`, safely award 500 bonus minutes
#    to all matching accounts in `df_telecom` in place!
# 2. Verify that accounts 501 and 503 received 500, while 502 and 504 remained 0.
# 3. Calculate the total bonus minutes distributed across all accounts and store in `total_bonus`.

# Write your code for Problem 4 below:




# ==============================================================================
# When you have completed your answers, save this file and say "check it"!
# ==============================================================================