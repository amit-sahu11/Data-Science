# ==============================================================================
# 📝 PRACTICE ARCHIVE — Session 1: Practice Set 2 (Pipelines, Lambdas & Functions)
# Topic: Unit Conversion Lambdas, Data Cleaning Sanitizers & Feature Engineering
# Status: 100% Mastered & Verified
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 1: Lambda Expression for Unit Conversion
# ------------------------------------------------------------------------------
# Student Solution:
mph_to_kmh = lambda mph: round(mph * 1.60934, 2)
converted_speed = mph_to_kmh(60)

# 👨‍🏫 TEACHER REVIEW — Problem 1: ✅ 100% PERFECT!
# Clean, compact lambda function evaluating to 96.56 km/h.


# ------------------------------------------------------------------------------
# Problem 2: Robust Data Cleaning Function with isinstance() Type Guard
# ------------------------------------------------------------------------------
# Student Solution:
def clean_price(raw_val):
    if not isinstance(raw_val, str) or raw_val.strip().upper() in ["N/A", "MISSING", ""]:
        return 0.0
    return float(raw_val.replace("$", "").replace(",", "").strip())

# 👨‍🏫 TEACHER REVIEW — Problem 2: ✅ 100% SOLVED & VERIFIED!
# `not isinstance(raw_val, str)` guards against non-strings, and null markers
# are gracefully mapped to 0.0. Clean strings become floats cleanly.


# ------------------------------------------------------------------------------
# Problem 3: Applying Cleaning Pipeline Across Dataset
# ------------------------------------------------------------------------------
raw_prices = ["$1,200.50", "N/A", " $45.00 ", "MISSING", "$3,450.00", ""]

# Student Solution:
cleaned_prices = [clean_price(x) for x in raw_prices]

# 👨‍🏫 TEACHER REVIEW — Problem 3: ✅ 100% PERFECT PIPELINE EXECUTION!
# Pipeline verified! Output matches target exactly:
#   [1200.5, 0.0, 45.0, 0.0, 3450.0, 0.0]


# ------------------------------------------------------------------------------
# Problem 4: Flexible Feature Engineering Function
# ------------------------------------------------------------------------------
# Student Solution:
def categorize_engagement(score, high_threshold=80, medium_threshold=50):
    if score >= high_threshold:
        return "High"
    elif score >= medium_threshold:
        return "Medium"
    else:
        return "Low"

result_1 = categorize_engagement(85)
result_2 = categorize_engagement(65, high_threshold=70, medium_threshold=60)

# 👨‍🏫 TEACHER REVIEW — Problem 4: ✅ 100% PERFECT!
# Clean handling of default arguments and keyword argument overrides:
# - result_1 -> "High"
# - result_2 -> "Medium"
