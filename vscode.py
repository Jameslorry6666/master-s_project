
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
#Read and view the data set
df = pd.read_csv('df_drop.csv')

# Add print statements to see the data
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())



print("=== DATASET ANALYSIS ===")
print(f"Shape: {df.shape} (rows, columns)")

print("\n--- First 5 Rows ---")
print(df.head())


print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Basic Statistics ---")
print(df.describe())

# Basic visualizations (if you have numeric columns)

# Basic visualizations (if you have numeric columns)
numeric_columns = df.select_dtypes(include=[np.number]).columns

if len(numeric_columns) > 0:
    print(f"\nNumeric columns: {list(numeric_columns)}")
    
    # Create a simple histogram for the first numeric column
    plt.figure(figsize=(10, 6))
    df[numeric_columns[0]].hist()
    plt.title(f'Distribution of {numeric_columns[0]}')
    plt.savefig('distribution.png')  # Save the plot
    print("Plot saved as 'distribution.png'")
else:
    print("No numeric columns found for visualization")