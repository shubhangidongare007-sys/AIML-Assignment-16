import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load file safely
df = pd.read_csv("insurance.csv", sep=None, engine='python')

# 2. Clean extra spaces from column names
df.columns = df.columns.str.strip()

# 3. Create a clean dictionary for final numeric data
numeric_data = {}
columns_to_find = ["age", "bmi", "children", "expenses"]

# 4. Forcefully convert text data into numbers, removing errors
for col in columns_to_find:
    if col in df.columns:
        numeric_data[col] = pd.to_numeric(df[col], errors='coerce')

# 5. Build the final clean DataFrame and drop any empty rows
num_df = pd.DataFrame(numeric_data).dropna()

# 6. Check if data exists and plot the heatmap
if not num_df.empty:
    plt.figure(figsize=(8, 6))
    sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm")
    plt.show()
else:
    print("Error: DataFrame is still empty. Please check the dataset format.")
