# 📊 Data Science Learning Tracker & Study Memory

## 👤 Student Profile & Objective
- **Student**: Amit
- **Goal**: Become strong in Data Science and practical programming from first principles to industry-level mastery.
- **Started**: 2026-09-26

---

## 🗺️ Master Curriculum Roadmap
- [x] **Phase 1: Python for Data Science & Algorithmic Problem Solving (COMPLETED ✅)**
  - [x] 1.0 Environment & Python 3.12 Setup
  - [x] 1.1 Python Memory Model & References vs Copies (`b = a` vs `b = a.copy()`)
  - [x] 1.2 Python Slicing & Indexing Mechanics (`[start:stop:step]`, half-open intervals)
  - [x] 1.3 Data Structures: Safe Dictionaries (`.get()`), Sets, and Frequency Maps
  - [x] 1.4 List Comprehensions & Vectorized Thinking
  - [x] 1.5 Functions, Lambda Expressions, and Custom Data Cleaning Pipelines
  - [x] 1.6 File Handling, Exception Handling, and Working with Raw Data Files (CSV, JSON)
- [x] **Phase 2: Numerical Computing & Vectorization (NumPy) (COMPLETED ✅)**
  - [x] 2.1 Arrays, Contiguous C-Memory, SIMD Vectorization & Constructors (`arange`, `linspace`)
  - [x] 2.2 2D Slicing, Multi-Axis Indexing, Axis Collapse (`axis=0/1`), Boolean Masking & `np.where`
  - [x] 2.3 Mathematical & Statistical Operations in NumPy (`std`, `var`, `argmin`, `argmax`, percentiles)
  - [x] 2.4 Broadcasting Mechanics & Array Reshaping (`reshape`, `transpose`, `newaxis`)
- [ ] **Phase 3: Data Manipulation & Wrangling (Pandas)**
  - [x] 3.1 Series and DataFrames (Architecture, `.values`/`.to_numpy()`, `.index`, Alignment, `.set_index()`)
  - [ ] 3.2 Filtering, Indexing, and Selecting Data (`.loc`, `.iloc`, Boolean Masking, Querying)
  - [ ] 3.3 Handling Missing Data, Outliers, and Cleaning
  - [ ] 3.4 GroupBy, Aggregations, and Pivoting
  - [ ] 3.5 Merging, Joining, and Reshaping Datasets
- [ ] **Phase 4: Exploratory Data Analysis (EDA) & Visualization**
  - [ ] 4.1 Data Distribution & Summary Statistics
  - [ ] 4.2 Matplotlib & Seaborn (Univariate, Bivariate, Multivariate Visualizations)
  - [ ] 4.3 Practical EDA Walkthrough on Real-World Datasets
- [ ] **Phase 5: Applied Mathematics & Statistics for Data Science**
  - [ ] 5.1 Descriptive Statistics (Central Tendency, Dispersion, Skewness, Kurtosis)
  - [ ] 5.2 Probability Distributions (Normal, Binomial, Poisson, Uniform)
  - [ ] 5.3 Inferential Statistics (Hypothesis Testing, p-values, Confidence Intervals, A/B Testing)
  - [ ] 5.4 Linear Algebra & Calculus Essentials (Vectors, Matrices, Dot Products, Gradients)
- [ ] **Phase 6: Classical Machine Learning (Scikit-Learn)**
  - [ ] 6.1 Supervised Learning - Regression (Linear, Ridge, Lasso, Evaluation Metrics)
  - [ ] 6.2 Supervised Learning - Classification (Logistic Regression, Decision Trees, Random Forests, SVM)
  - [ ] 6.3 Model Evaluation & Validation (Cross-Validation, Confusion Matrix, ROC-AUC)
  - [ ] 6.4 Unsupervised Learning (K-Means, Hierarchical Clustering, PCA)
  - [ ] 6.5 Hyperparameter Tuning & ML Pipelines
- [ ] **Phase 7: End-to-End Projects & Advanced DS**
  - [ ] 7.1 Feature Engineering & Preprocessing Pipeline
  - [ ] 7.2 Full Machine Learning Capstone Project

---

## 📈 Current Status Summary
- **Current Phase**: Phase 3: Data Manipulation & Wrangling with Pandas (Topic 3.1 Mastered!)
- **Python Version**: Python 3.12.10 installed & verified
- **Topics Completed**:
  - Python Environment & Libraries Setup
  - Memory references & `.copy()` protection
  - Slicing interval mechanics `[start:stop)`
  - Dictionary `.get()` safe extraction
  - List comprehensions with filtering
  - Lambda expressions for inline transformations
  - Custom Data Cleaning Pipelines (`clean_price`) with type guards & null handling
  - Feature engineering functions with default & keyword parameters
  - File Ingestion (`with open`), Context Managers, `as f` file handles
  - Tabular CSV ingestion with `csv.DictReader`
  - Hierarchical JSON parsing with `json.load()`
  - Exporting tabular data with `csv.DictWriter`
  - Robust exception handling (`try...except FileNotFoundError`)
  - NumPy ndarray memory architecture (contiguous C-memory vs scattered Python lists)
  - Array metadata: `.shape`, `.dtype`, `.ndim`, `.size`, `.nbytes`
  - Hardware SIMD vectorization (no loops)
  - Sequence constructors: `np.arange` vs `np.linspace`
  - Multi-array mathematical modeling (Vectorized BMI calculation)
  - Multi-dimensional 2D slicing (`matrix[row_slice, col_slice]`)
  - Axis mechanics: `axis=0` (vertical drop / collapse rows) vs `axis=1` (horizontal walk / collapse columns)
  - Boolean masking with bitwise operators (`&`, `|`, `~`) and operator precedence parentheses
  - Vectorized conditional replacement with `np.where()`
  - Array views vs independent copies in memory
  - Statistical dispersion metrics (`std`, `var`, Z-Score outlier detection)
  - Extrema position indexing (`argmin`, `argmax` along axes)
  - Array reshaping & transposing (`reshape`, `-1` wildcard, `transpose`)
  - Broadcasting engine (two golden rules, zero-stride virtual expansion, feature mean-centering)
  - Pandas Series architecture (NumPy `.to_numpy()` data buffer + Index object)
  - Automatic label-based index alignment (`+` vs `.add(fill_value=0)`)
  - Heterogeneous DataFrame creation from dictionaries & inspection (`.dtypes`, `.shape`)
  - Custom primary key indexing with `.set_index()`
  - Vectorized financial feature engineering on DataFrames (Debt-to-Income calculation)
- **Topics Currently Learning**:
  - Phase 3.2: Filtering, Indexing & Selecting Data (`.loc` label vs `.iloc` integer position indexing)
- **Strong Areas**:
  - Series vs DataFrame mental model
  - Automatic index alignment
  - Vectorized feature engineering without loops
  - NumPy contiguous memory & broadcasting
- **Areas Solidified & Revised**:
  - Distinguishing DataFrame variables from string lists: calling methods directly on `df_customers` rather than `["df_customer"]`.
- **Questions Wrong**:
  - Phase 3 Set 1: 0 wrong! (Self-corrected syntax cleanly on first prompt).
- **Practice Exercises Completed**: 7 sets (28 problems total, 100% Mastered)
- **Recommended Next Topic**: Phase 3.2: Advanced Indexing & Selection (`loc` vs `iloc`, Conditional Filtering on DataFrames)

---

## 📝 Study Memory Log

### Session 2 (NumPy 2D Slicing, Axes & Boolean Masking Mastery)
- **DATE**: 2026-09-26
- **SUBJECT**: Data Science & Practical Programming
- **TOPICS COMPLETED**: 2D Matrix Slicing (`matrix[rows, cols]`), Axis Mechanics (`axis=0` vertical drop vs `axis=1` horizontal walk), Boolean Masking (`&`, `|`), Vectorized `np.where()` classification.
- **TOPICS IN PROGRESS**: Phase 2.3 - Statistical Metrics (`std`, `var`, `argmin`, `argmax`) & Broadcasting
- **STRONG AREAS**: Axis comprehension, sub-matrix extraction, conditional filtering, `np.where()` flagging.
- **WEAK AREAS**: None — 100% mastery achieved across all 4 problems in Set 2 on the first attempt!
- **QUESTIONS I GOT WRONG**: None in Set 2 (100% accuracy).
- **PRACTICE COMPLETED**: Phase 2 Practice Set 2 (Archived in `practice_archive/Session_02_NumPy_Vectorization/`).
- **NEXT TOPIC**: Phase 2.3 - Statistical Aggregations & Array Broadcasting
- **REVISION NEEDED**: None needed — all code archived in practice_archive/.

### Session 3 (NumPy Statistics, Argmax, Reshaping & Broadcasting Mechanics)
- **DATE**: 2026-10-01
- **SUBJECT**: Data Science & Numerical Computing (NumPy)
- **TOPICS COMPLETED**: Statistical dispersion (`std`, `var`, Z-Score outlier detection), Extrema positioning (`argmin`, `argmax` along axes), Memory reshaping & transposing (`reshape`, `-1` wildcard, `transpose`), Vectorized broadcasting engine & feature mean-centering.
- **TOPICS IN PROGRESS**: Phase 3.1 - Pandas Series & DataFrames Architecture
- **STRONG AREAS**: Axis collapse mechanics (`axis=0` vs `axis=1`), Z-score anomaly filtering, broadcasting rules & mean-centering.
- **WEAK AREAS**: None — 100% mastery achieved after immediate correction of column slicing in Practice Set 3!
- **QUESTIONS I GOT WRONG**: None (self-corrected with 1 prompt).
- **PRACTICE COMPLETED**: Phase 2 Practice Set 3 (Archived in `practice_archive/Session_02_NumPy_Vectorization/Practice_Set_03_Stats_Reshape_Broadcasting.py`).
- **NEXT TOPIC**: Phase 3.1: Introduction to Pandas (Series, DataFrames, Memory & Indexing)
- **REVISION NEEDED**: None needed — 24/24 problems across 6 sets mastered.

### Session 4 (Pandas Architecture: Series, DataFrames & Alignment)
- **DATE**: 2026-10-02
- **SUBJECT**: Data Science & Tabular Manipulation (Pandas)
- **TOPICS COMPLETED**: Pandas Series anatomy (NumPy `.to_numpy()` data buffer + Index object), Automatic label-based index alignment (`+` vs `.add(fill_value=0)`), DataFrame construction from heterogeneous dicts, `.set_index()` custom indexing, Vectorized feature engineering on DataFrames.
- **TOPICS IN PROGRESS**: Phase 3.2 - Advanced Indexing & Selection (`loc` vs `iloc`, Boolean Filtering on DataFrames)
- **STRONG AREAS**: Series & DataFrame concepts, automatic alignment handling, vectorized feature creation.
- **WEAK AREAS**: None — 100% accuracy achieved across all 4 problems in Set 1!
- **QUESTIONS I GOT WRONG**: None (clean first-prompt correction).
- **PRACTICE COMPLETED**: Phase 3 Practice Set 1 (Archived in `practice_archive/Session_03_Pandas_Manipulation/Practice_Set_01_Series_DataFrames_Alignment.py`).
- **NEXT TOPIC**: Phase 3.2: Filtering, Indexing & Selecting Data with `.loc` and `.iloc`
- **REVISION NEEDED**: None needed — 28/28 problems across 7 sets mastered.


