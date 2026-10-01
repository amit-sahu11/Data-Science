# ==============================================================================
# 📝 PRACTICE.py — Phase 2: Practice Set 3
# Topic: Statistical Dispersion, Argmax, Reshaping & Broadcasting Mechanics
# ==============================================================================
# Instructions:
# Write your code directly under each problem where marked.
# Do not delete or overwrite the problem setup code.
# When you have completed all problems, save this file and say: "check it"!
# ==============================================================================
import numpy as np

# ------------------------------------------------------------------------------
# Problem 1: Statistical Dispersion & Z-Score Anomaly Detection
# ------------------------------------------------------------------------------
# In web infrastructure, server latency spikes indicate database bottlenecks.
# Below are response latency measurements (in milliseconds) from a web service:
latencies = np.array([24.5, 26.1, 25.0, 24.8, 120.5, 25.4, 25.2, 26.0])

# Task:
# 1. Compute the arithmetic mean of latencies and store in `mean_lat`.
# 2. Compute the standard deviation of latencies and store in `std_lat`.
# 3. Compute the Z-Score for each data point: z = (latencies - mean) / std.
#    Store the resulting array in `z_scores`.
# 4. Using boolean masking on `z_scores`, extract all raw latency values from
#    `latencies` where the z_score is strictly greater than 2.0 (anomalies).
#    Store these in `outliers`.

# Write your code for Problem 1 below:

mean_lat = np.mean(latencies)
std_lat = np.std(latencies)
z_scores = (latencies-mean_lat)/std_lat
outliers = latencies[z_scores>2.0]

# 👨‍🏫 TEACHER REVIEW:
# Status: 🌟 100% PERFECT! Flawless Mastery!
# What's Great:
#   - Mean, standard deviation, and vectorized Z-Score calculations are 100% spot-on!
#   - Direct boolean index extraction `latencies[z_scores > 2.0]` cleanly isolates the anomaly ([120.5]).
#   - Memory efficient, SIMD-accelerated outlier detection!




# ------------------------------------------------------------------------------
# Problem 2: Business Decision-Making with Argmin & Argmax
# ------------------------------------------------------------------------------
# A retail company tracks 4 store branches across 6 consecutive months (Jan to Jun).
# Each row represents a store [Store 0 to 3], and each column is a month [Month 0 to 5]:
store_sales = np.array([
    [50, 62, 58, 70, 65, 80],   # Store 0
    [45, 55, 60, 58, 62, 64],   # Store 1
    [72, 75, 80, 85, 90, 95],   # Store 2
    [30, 32, 40, 38, 42, 45]    # Store 3
])

# Task:
# 1. For EACH STORE (row-wise), find the index of the month that had the PEAK sales.
#    (Walk horizontally across columns, collapsing axis 1).
#    Store the array of month indices in `best_month_per_store`.
# 2. For EACH MONTH (column-wise), find the index of the store that was the TOP PERFORMER.
#    (Walk vertically down rows, collapsing axis 0).
#    Store the array of store indices in `top_store_per_month`.

# Write your code for Problem 2 below:

best_month_per_store = np.argmax(store_sales,axis=1)
print(best_month_per_store)

top_store_per_month = np.argmax(store_sales,axis=0)
print(top_store_per_month)

# 👨‍🏫 TEACHER REVIEW:
# Status: 🌟 100% PERFECT! Flawless!
# What's Great:
#   - You nailed the 2D axis mechanics:
#     * Row-wise peak across columns = axis=1 (output: [5, 5, 5, 5] -> Month 5 was peak for all stores).
#     * Column-wise top store across rows = axis=0 (output: [2, 2, 2, 2, 2, 2] -> Store 2 won every month).
#   - Pure NumPy idiomatic mastery!



# ------------------------------------------------------------------------------
# Problem 3: Array Reshaping & ML Feature Vector Preparation
# ------------------------------------------------------------------------------
# Machine learning algorithms (like Linear Regression in Scikit-Learn) strictly require
# 2D matrices where rows = samples and columns = features.
# A continuous flat stream of sensor readings:
sensor_stream = np.arange(10, 130, 10)  # 12 readings: [10, 20, 30, ..., 120]

# Task:
# 1. Reshape `sensor_stream` into a 2D matrix of 3 rows and 4 columns.
#    Store in `grid_3x4`.
# 2. Transpose `grid_3x4` so its shape becomes (4, 3) (swapping rows & columns).
#    Store in `grid_transposed`.
# 3. Take the first column of `grid_transposed` (which is a 1D array of 4 items)
#    and reshape it into a 2D column vector of shape (4, 1) using `-1` wildcard.
#    Store in `col_vector`.

# Write your code for Problem 3 below:

grid_3x4 = np.reshape(sensor_stream,(3,4))
print(grid_3x4)

grid_transposed = np.transpose(grid_3x4)
print(grid_transposed)

first_col = grid_transposed[:,0]
col_vector = np.reshape(first_col,(-1,1))
print(col_vector)

# 👨‍🏫 TEACHER REVIEW:
# Status: 🌟 100% PERFECT! Flawless!
# What's Great:
#   - Task 1: Reshaping (12,) -> (3, 4) is 100% correct!
#   - Task 2: Transposing (3, 4) -> (4, 3) is 100% correct!
#   - Task 3: 2D column slicing `grid_transposed[:, 0]` followed by `.reshape(-1, 1)` cleanly creates
#     the exact (4, 1) 2D column feature vector required by Scikit-Learn!
#   - Outstanding correction!



# ------------------------------------------------------------------------------
# Problem 4: Broadcasting Mechanics — Feature Normalization (Mean-Centering)
# ------------------------------------------------------------------------------
# In Machine Learning, centering data (subtracting the feature mean) speeds up
# gradient descent and prevents features with larger numbers from dominating.
# A housing dataset with 3 houses (rows) and 3 features [Area, Bedrooms, Age] (columns):
houses = np.array([
    [18.0, 3.0, 15.0],   # House 0
    [24.0, 4.0,  5.0],   # House 1
    [12.0, 2.0, 25.0]    # House 2
])

# Task:
# 1. Calculate the mean of EACH FEATURE across all houses (collapse axis 0).
#    Store in `feature_means`. (Shape should be (3,)).
# 2. Using NumPy Broadcasting, subtract `feature_means` directly from `houses`.
#    NumPy will automatically stretch the 1D (3,) array across all 3 rows of the (3, 3) matrix!
#    Store the centered matrix in `normalized_houses`.
# 3. Verify: Calculate the mean of each feature in `normalized_houses` (axis 0)
#    and store in `centered_means`. (They should all be virtually 0.0!).

# Write your code for Problem 4 below:

feature_means = np.mean(houses,axis=0)
print(feature_means)

normalized_houses = np.subtract(houses,feature_means)
print(normalized_houses)

centered_means = np.mean(normalized_houses,axis=0)
print(centered_means)

# 👨‍🏫 TEACHER REVIEW:
# Status: 🌟 100% PERFECT! Flawless Mastery!
# What's Great:
#   - Feature mean calculation collapsing axis=0 gave exactly [18.0, 3.0, 15.0].
#   - Broadcasting worked seamlessly: subtracting shape (3,) from shape (3, 3) automatically
#     stretched across rows without loops or manual duplication.
#   - Centered means verified to [0., 0., 0.] — data is perfectly normalized for Machine Learning!




# ==============================================================================
# When you have completed your answers, save this file and say "check it"!
# ==============================================================================