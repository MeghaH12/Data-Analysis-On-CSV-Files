import pandas as pd

# Load CSV file
file_path = "data.csv"   # <-- change to your CSV file name
df = pd.read_csv(file_path)

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Basic info
print("\nDataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Column names
print("\nColumns in dataset:")
print(df.columns.tolist())

# Correlation between numeric columns
print("\nCorrelation Matrix:")
print(df.corr())

# Example: Group by (if categorical column exists, e.g., 'Category')
if "Category" in df.columns:
    print("\nGroup by Category:")
    print(df.groupby("Category").mean())