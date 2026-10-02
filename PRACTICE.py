# ==============================================================================
# 📝 PRACTICE.py — Phase 3: Practice Set 1
# Topic: Pandas Architecture — Series, DataFrames & Automatic Index Alignment
# ==============================================================================
# Instructions:
# Write your code directly under each problem where marked.
# Do not delete or overwrite the problem setup code.
# When you have completed all problems, save this file and say: "check it"!
# ==============================================================================
import pandas as pd
import numpy as np

# ------------------------------------------------------------------------------
# Problem 1: Series Anatomy — Data Buffer vs Labeled Index
# ------------------------------------------------------------------------------
# In e-commerce analytics, product stock levels are tracked by unique SKU codes.
# Below are stock counts and their corresponding product SKU strings:
skus = ["SKU_LAPTOP", "SKU_MOUSE", "SKU_KEYBOARD", "SKU_MONITOR"]
stock_counts = [45, 230, 115, 60]

# Task:
# 1. Create a Pandas Series named `inventory` using `stock_counts` as the data
#    and `skus` as the index labels.
# 2. Extract the underlying raw NumPy ndarray buffer from `inventory` and store in `raw_counts`.
# 3. Extract the Index object from `inventory` and store in `sku_labels`.
# 4. Access the stock count for "SKU_KEYBOARD" using label indexing and store in `kb_stock`.

# Write your code for Problem 1 below:


inventory = pd.Series(stock_counts,index = skus)

raw_counts = inventory.to_numpy()
print(raw_counts)

sku_labels = inventory.index
print(sku_labels)

kb_stock = inventory["SKU_KEYBOARD"]
print(kb_stock)

# 👨‍🏫 TEACHER REVIEW:
# Status: 🌟 100% PERFECT! Flawless!
# What's Great:
#   - Created Series with custom labels seamlessly.
#   - `.to_numpy()` is the modern, idiomatic standard to grab the underlying buffer!
#   - `.index` and label lookup `inventory["SKU_KEYBOARD"]` are 100% spot-on.


# ------------------------------------------------------------------------------
# Problem 2: The Superpower of Automatic Index Alignment
# ------------------------------------------------------------------------------
# Two branch stores report their revenue for various product categories.
# Notice that Store B sells Tablets, but Store A does not; Store A sells Monitors,
# but Store B does not.
store_a_rev = pd.Series([12000, 4500, 8000], index=["Laptops", "Mice", "Monitors"])
store_b_rev = pd.Series([9500, 3200, 6000], index=["Laptops", "Mice", "Tablets"])

# Task:
# 1. Add `store_a_rev` and `store_b_rev` together using direct addition (+)
#    and store in `total_direct`.
#    Observe: Categories not present in both will become NaN!
# 2. To safely handle missing categories, use the `.add()` method with `fill_value=0`
#    so missing categories are treated as 0 instead of NaN.
#    Store the result in `total_safe`.

# Write your code for Problem 2 below:

total_direct = store_a_rev + store_b_rev
print(total_direct)

total_safe = store_a_rev.add(store_b_rev,fill_value = 0)
print(total_safe)

# 👨‍🏫 TEACHER REVIEW:
# Status: 🌟 100% PERFECT! Flawless!
# What's Great:
#   - Direct addition (+) showed how non-overlapping categories become NaN.
#   - Safe `.add(..., fill_value=0)` correctly handled missing values across branches!


# ------------------------------------------------------------------------------
# Problem 3: DataFrame Construction & Metadata Inspection
# ------------------------------------------------------------------------------
# Build a customer dataset containing heterogeneous data types (strings, ints, floats, booleans).
# Raw data dictionary:
customer_data = {
    "customer_id": [101, 102, 103, 104],
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [28, 45, 34, 52],
    "spend_usd": [250.75, 1200.50, 45.00, 890.25],
    "is_premium": [True, True, False, True]
}

# Task:
# 1. Construct a Pandas DataFrame from `customer_data` and store in `df_customers`.
# 2. Set the index of `df_customers` to be the "customer_id" column (using `.set_index()`).
#    Store the updated DataFrame in `df_indexed`.
# 3. Extract the "spend_usd" column from `df_indexed` as a Series and store in `spend_series`.
# 4. Verify that `type(spend_series)` is a `pd.Series` and inspect its `.dtype`.
#    Store its dtype in `spend_dtype`.

# Write your code for Problem 3 below:

df_customers = pd.DataFrame(customer_data)

df_indexed = df_customers.set_index("customer_id")

spend_series = df_indexed["spend_usd"]

spend_dtype = spend_series.dtype

# 👨‍🏫 TEACHER REVIEW:
# Status: 🌟 100% PERFECT! Flawless!
# What's Great:
#   - Clean DataFrame construction from heterogeneous dictionary.
#   - `.set_index("customer_id")` correctly designated the primary key row index.
#   - Column extraction `df_indexed["spend_usd"]` verified as a `pd.Series` with `.dtype == float64`.
#   - Outstanding correction!



# ------------------------------------------------------------------------------
# Problem 4: Vectorized Feature Engineering on DataFrames
# ------------------------------------------------------------------------------
# In financial risk analysis, we calculate customer debt-to-income ratio (DTI)
# and flag high-risk borrowers.
employee_data = {
    "monthly_income": [5000.0, 3200.0, 8500.0, 2100.0],
    "monthly_debt": [1500.0, 1600.0, 1700.0, 1260.0]
}
df_finance = pd.DataFrame(employee_data)

# Task:
# 1. Create a new column "dti_ratio" in `df_finance` calculated as:
#    dti_ratio = monthly_debt / monthly_income
#    (Do this with pure vectorization — NO for-loops!).
# 2. Create a new boolean column "high_risk" in `df_finance` that is True
#    if "dti_ratio" is strictly greater than 0.40 (40%), otherwise False.
# 3. Calculate the average DTI ratio across all employees and store in `avg_dti`.

# Write your code for Problem 4 below:

df_finance["dti_ratio"] = df_finance["monthly_debt"] / df_finance["monthly_income"]

df_finance["high_risk"] = df_finance["dti_ratio"] > 0.40

avg_dti = df_finance["dti_ratio"].mean()
print(avg_dti)

# 👨‍🏫 TEACHER REVIEW:
# Status: 🌟 100% PERFECT! Flawless Mastery!
# What's Great:
#   - Pure vectorized division `monthly_debt / monthly_income` without loops!
#   - Vectorized boolean flag `dti_ratio > 0.40` generated exact True/False Series.
#   - Summary metric `avg_dti = ...mean()` computed accurately (mean DTI = 0.428).



# ==============================================================================
# When you have completed your answers, save this file and say "check it"!
# ==============================================================================