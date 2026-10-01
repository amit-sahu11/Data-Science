# ==============================================================================
# 📝 PRACTICE ARCHIVE — Session 1: Practice Set 3 (File I/O, CSV/JSON & Exceptions)
# Topic: Context Managers, csv.DictReader/DictWriter, json.load, Exception Handling
# Status: 100% Mastered & Verified
# ==============================================================================
import csv
import json

# ------------------------------------------------------------------------------
# Problem 1: Crash-Proof File Ingestion (Exception Handling)
# ------------------------------------------------------------------------------
def safe_read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found"

content_1 = safe_read_file("sample_sales.csv")
content_2 = safe_read_file("missing_dataset.csv")

# 👨‍🏫 TEACHER REVIEW — Problem 1: ✅ 100% PERFECT!
# Excellent! `try...except FileNotFoundError` returns a safe fallback message
# without crashing the process.


# ------------------------------------------------------------------------------
# Problem 2: Tabular Ingestion with csv.DictReader & Aggregation
# ------------------------------------------------------------------------------
with open("sample_sales.csv", 'r') as f:
    reader = csv.DictReader(f)
    total_revenue = 0.0
    for row in reader:
        revenue_per_row = float(row["price"]) * int(row["units_sold"])
        total_revenue += revenue_per_row
print(total_revenue)  # Output: 15420.0

# 👨‍🏫 TEACHER REVIEW — Problem 2: ✅ 100% PERFECT!
# Correct type conversion and loop aggregation. Result: 15420.0.


# ------------------------------------------------------------------------------
# Problem 3: Parsing Nested JSON Data
# ------------------------------------------------------------------------------
with open("sensor_data.json", 'r') as f:
    sensor_info = json.load(f)
    station = sensor_info["station_id"]
    current_temp = sensor_info["readings"][0]["value"]

# 👨‍🏫 TEACHER REVIEW — Problem 3: ✅ 100% PERFECT!
# Nested JSON parsed into dict and list. station = 'STATION_NORTH_01', temp = 24.5.


# ------------------------------------------------------------------------------
# Problem 4: Writing Cleaned Data Back to a New CSV File
# ------------------------------------------------------------------------------
summary_records = [
    {"category": "Electronics", "items_count": 3},
    {"category": "Office", "items_count": 2}
]

with open("sales_summary.csv", "w", newline="") as f:
    fieldnames = ["category", "items_count"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(summary_records)

# 👨‍🏫 TEACHER REVIEW — Problem 4: ✅ 100% PERFECT!
# Correct use of `newline=""`, `writeheader()`, and `writerows()`.
