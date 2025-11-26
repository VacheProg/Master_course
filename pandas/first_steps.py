"""
Pandas Basic Usage Teaching File
This file is intended for a basic course to demonstrate fundamental Pandas operations:
 - Series
 - DataFrames
 - Reading/Writing CSV
 - Basic operations
 - Filtering/Sorting
 - GroupBy
 - Merging/Joining
 - Handling missing values
"""

import pandas as pd

# -----------------------------
# 1. Creating a Series
# -----------------------------
series_example = pd.Series([10, 20, 30, 40], name="A")
print("Series example:")
print(series_example)
print("\n")

# -----------------------------
# 2. Creating a DataFrame
# -----------------------------
# Creating a DataFrame from a dictionary
people_df = pd.DataFrame({
    "name": ["Anna", "Mark", "John"],
    "age": [25, 32, 29],
    "salary": [500, 700, 600]
})
print("People DataFrame:")
print(people_df)
print("\n")

# -----------------------------
# 3. Reading and Writing CSV
# -----------------------------
# Writing DataFrame to CSV
people_df.to_csv("people.csv", index=False)

# Reading CSV back into DataFrame
df_from_csv = pd.read_csv("people.csv")
print("DataFrame loaded from CSV:")
print(df_from_csv)
print("\n")

# -----------------------------
# 4. Basic DataFrame Operations
# -----------------------------
# Selecting a single column
print("Ages:")
print(people_df["age"])
print("\n")

# Adding a new column
people_df["age_plus_ten"] = people_df["age"] + 10
print("DataFrame with new column:")
print(people_df)
print("\n")

# Filtering rows
adults_df = people_df[(people_df["age"] > 28)]
print("People older than 28:")
print(adults_df)
print("\n")

# Sorting
sorted_df = people_df.sort_values(by="salary", ascending=False)
print("Sorted by salary descending:")
print(sorted_df)
print("\n")

# -----------------------------
# 5. Handling Missing Values
# -----------------------------
data_with_missing = pd.DataFrame({
    "A": [1, 2, None, 4, '10'],
    "B": ["x", None, "z", "w", 'k']
})
print("Data with missing values:")
print(data_with_missing)
print("\n")
# Fill missing values
data_filled = data_with_missing.fillna({"A": 0, "B": "unknown"})
print("Missing values filled:")
print(data_filled)
print("\n")

# Drop missing rows
cleaned_data = data_with_missing.dropna()
print("Dropped rows with missing values:")
print(cleaned_data)
print("\n")

# -----------------------------
# 6. GroupBy Operations
# -----------------------------
company_df = pd.DataFrame({
    "department": ["Sales", "Sales", "IT", "IT", "HR"],
    "employee": ["A", "B", "C", "D", "E"],
    "salary": [500, 600, 800, 750, 400]
})

print("Company DataFrame:")
print(company_df)
print("\n")

# Group by department
salary_grouped = company_df.groupby("department").salary.mean()
print("Average salary per department:")
print(salary_grouped)
print("\n")

# -----------------------------
# 7. Merging / Joining
# -----------------------------
left_df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Anna", "Mark", "John"],
    "name_new": ["Anna", "Mark", "John"],
})

right_df = pd.DataFrame({
    "id": [1, 2, 4],
    "country": ["Armenia", "USA", "Canada"],
    "country_new": ["Armenia", "USA", "Canada"],
})

# Inner join
inner_join = pd.merge(left_df, right_df, on="id", how="inner")
print("Inner join:")
print(inner_join)
print("\n")

# Left join
left_join = pd.merge(left_df, right_df, on="id", how="left")
print("Left join:")
print(left_join)
print("\n")

# Outer join
outer_join = pd.merge(left_df, right_df, on="id", how="outer")
print("Outer join:")
print(outer_join)
print("\n")

# -----------------------------
# 8. Saving final result
# -----------------------------
outer_join.to_csv("joined_output.csv", index=False)
print("Final joined CSV saved as joined_output.csv")
