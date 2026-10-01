# ==============================================================================
# 📝 PRACTICE ARCHIVE — Session 2: Practice Set 1 (NumPy Arrays & Vectorization)
# Topic: Ndarray Anatomy (.shape, .dtype, .ndim), Vectorized Math, arange vs linspace, Vectorized BMI
# Status: 100% Mastered & Verified
# ==============================================================================
import numpy as np

# ------------------------------------------------------------------------------
# Problem 1: Creating Ndarrays & Inspecting Array Anatomy
# ------------------------------------------------------------------------------
sensor_matrix = np.array([[12.5, 14.0, 15.5], [18.0, 20.5, 22.0]])
matrix_shape = sensor_matrix.shape
matrix_dtype = sensor_matrix.dtype
matrix_ndim = sensor_matrix.ndim
print(sensor_matrix, matrix_shape, matrix_dtype, matrix_ndim)

# 👨‍🏫 TEACHER REVIEW — Problem 1: ✅ 100% PERFECT!
# - matrix_shape: (2, 3) -> 2 rows, 3 columns
# - matrix_dtype: float64 (homogeneous 64-bit floats)
# - matrix_ndim:  2 (2-dimensional matrix)


# ------------------------------------------------------------------------------
# Problem 2: The Magic of Vectorization (Zero For-Loops!)
# ------------------------------------------------------------------------------
prices_eur = np.array([50.0, 120.0, 30.0, 250.0, 80.0])
final_prices_usd = (prices_eur * 1.08) + 5.0

# 👨‍🏫 TEACHER REVIEW — Problem 2: ✅ 100% PERFECT!
# Applied element-wise scaling and translation across array simultaneously.
# Output: [ 59.  134.6  37.4 275.   91.4]


# ------------------------------------------------------------------------------
# Problem 3: Building Sequences with np.arange() vs np.linspace()
# ------------------------------------------------------------------------------
even_range = np.arange(10, 30, 2)
linear_points = np.linspace(0.0, 1.0, 5)

# 👨‍🏫 TEACHER REVIEW — Problem 3: ✅ 100% PERFECT!
# - even_range: [10 12 14 16 18 20 22 24 26 28] (step 2, stop 30 exclusive)
# - linear_points: [0.   0.25 0.5  0.75 1.  ] (5 exact linearly spaced points)


# ------------------------------------------------------------------------------
# Problem 4: Real-World Vectorized Health Analytics (BMI Calculation)
# ------------------------------------------------------------------------------
weights = np.array([70.0, 85.0, 60.0, 95.0, 52.0])      # in kg
heights = np.array([1.75, 1.80, 1.65, 1.72, 1.60])      # in meters

patient_bmis = np.round((weights / (heights ** 2)), 2)

# 👨‍🏫 TEACHER REVIEW — Problem 4: ✅ 100% PERFECT & VERIFIED!
# Vectorized BMI formula: [22.86, 26.23, 22.04, 32.11, 20.31] for all 5 patients.
