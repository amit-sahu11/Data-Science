# ==============================================================================
# 📝 PRACTICE ARCHIVE — Session 2: Practice Set 2 (2D Slicing, Axes & Boolean Masking)
# Topic: Multi-Dimensional Slicing, axis=0/1 Aggregations, Boolean Masking, np.where
# Status: 100% Mastered & Verified
# ==============================================================================
import numpy as np

# ------------------------------------------------------------------------------
# Problem 1: Multi-Dimensional 2D Slicing (Rows & Columns)
# ------------------------------------------------------------------------------
financials = np.array([
    [100, 60, 40, 10],   # Q1
    [120, 70, 50, 12],   # Q2
    [150, 80, 70, 15],   # Q3
    [200, 95, 105, 20]   # Q4
])

# Student Solution:
q3_data = financials[2, :]
profit_column = financials[:, 2]
mid_year_core = financials[1:3, 1:3]

# 👨‍🏫 TEACHER REVIEW — Problem 1: ✅ 100% PERFECT!
# - q3_data: [150, 80, 70, 15]
# - profit_column: [40, 50, 70, 105]
# - mid_year_core: [[70, 50], [80, 70]]


# ------------------------------------------------------------------------------
# Problem 2: Matrix Aggregation along Axes (axis=0 vs axis=1)
# ------------------------------------------------------------------------------
scores = np.array([
    [85, 90, 78],   # Student 0
    [70, 65, 80],   # Student 1
    [95, 92, 88],   # Student 2
    [60, 55, 72]    # Student 3
])

# Student Solution:
subject_averages = scores.mean(axis=0)
student_totals = scores.sum(axis=1)

# 👨‍🏫 TEACHER REVIEW — Problem 2: ✅ 100% PERFECT!
# - subject_averages (axis=0, vertical drop): [77.5, 75.5, 79.5]
# - student_totals (axis=1, horizontal walk): [253, 215, 275, 187]


# ------------------------------------------------------------------------------
# Problem 3: Boolean Masking (SQL WHERE in Python)
# ------------------------------------------------------------------------------
temps = np.array([28.5, 36.2, 19.4, 42.1, 31.0, 9.5, 38.8, 14.2])

# Student Solution:
hot_temps = temps[temps > 35.0]
extreme_temps = temps[(temps < 15.0) | (temps > 40.0)]

# 👨‍🏫 TEACHER REVIEW — Problem 3: ✅ 100% PERFECT!
# - hot_temps: [36.2, 42.1, 38.8]
# - extreme_temps: [42.1, 9.5, 14.2] (Bitwise | with parentheses)


# ------------------------------------------------------------------------------
# Problem 4: Conditional Data Flagging with np.where()
# ------------------------------------------------------------------------------
defect_scores = np.array([12, 45, 82, 33, 90, 15, 68])

# Student Solution:
qc_status = np.where(defect_scores <= 50, "APPROVED", "REJECTED")

# 👨‍🏫 TEACHER REVIEW — Problem 4: ✅ 100% PERFECT!
# Output: ['APPROVED', 'APPROVED', 'REJECTED', 'APPROVED', 'REJECTED', 'APPROVED', 'REJECTED']
