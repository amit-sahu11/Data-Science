# ==============================================================================
# 📝 PRACTICE ARCHIVE — Session 1: Practice Set 1 (Foundations & Core Mechanics)
# Topic: Memory References, Slicing, Dictionaries & Comprehensions
# Status: 100% Mastered & Verified
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 1: Preventing Unintended Mutation (References vs Copies)
# ------------------------------------------------------------------------------
raw_readings = [10.2, 14.5, 18.9, 21.0]

# Student Solution:
cleaned_readings = raw_readings.copy()
cleaned_readings.append(99.9)

print("cleaned_readings", cleaned_readings)
print("raw_readings", raw_readings)

# 👨‍🏫 TEACHER REVIEW — Problem 1: ✅ 100% PERFECT!
# Excellent! You used `.copy()` which allocated a brand-new list at a new memory
# address. Appending 99.9 to `cleaned_readings` left `raw_readings` completely untouched.


# ------------------------------------------------------------------------------
# Problem 2: Slicing Extraction with Exact Intervals
# ------------------------------------------------------------------------------
temperatures = [22, 24, 25, 27, 26, 23, 21]

# Student Solution:
mid_week = temperatures[1:5]

# 👨‍🏫 TEACHER REVIEW — Problem 2: ✅ 100% PERFECT!
# Spot on! Applied the half-open interval rule [start : stop) flawlessly.
# Friday is index 4, so setting stop index to 5 extracts [24, 25, 27, 26].


# ------------------------------------------------------------------------------
# Problem 3: Clean & Safe Data Extraction with .get()
# ------------------------------------------------------------------------------
customer_info = {
    "name": "Sarah",
    "city": "Mumbai",
    "loyalty_points": 150
}

# Student Solution:
customer_age = customer_info.get("age", 18)
customer_city = customer_info.get("city", "Unknown")

# 👨‍🏫 TEACHER REVIEW — Problem 3: ✅ 100% EXCELLENT!
# `.get()` safely retrieves values or falls back to defaults without raising KeyError.


# ------------------------------------------------------------------------------
# Problem 4: List Comprehension Data Filtering
# ------------------------------------------------------------------------------
sales = [120, 45, 300, 85, 520, 60]

# Student Solution:
taxed_large_sales = [x * 1.10 for x in sales if x >= 100]

# 👨‍🏫 TEACHER REVIEW — Problem 4: ✅ 100% PERFECT!
# Clean vectorized comprehension syntax: [132.0, 330.0, 572.0].
