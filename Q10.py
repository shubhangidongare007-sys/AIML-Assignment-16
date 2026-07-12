import pandas as pd
import numpy as np

# 1. Load the dataset safely using tab separator
df = pd.read_csv('insurance.csv', sep='\t')

# 2. Fix all column headers to lowercase
df.columns = df.columns.str.lower()

# 3. Clean and convert data columns to absolute numeric values to stop all TypeErrors
df['age'] = pd.to_numeric(df['age'].astype(str).str.extract(r'(\d+)')[0], errors='coerce')
df['bmi'] = pd.to_numeric(df['bmi'].astype(str).str.extract(r'([\d\.]+)')[0], errors='coerce')
df['expenses'] = pd.to_numeric(df['expenses'].astype(str).str.extract(r'([\d\.]+)')[0], errors='coerce')

# 4. Drop any blank row created during string cleaning
df = df.dropna(subset=['age', 'bmi', 'expenses'])

# 5. Print the absolute final assignment data to the terminal
print("\n" + "="*50)
print("             Q10: LAB ASSIGNMENT OUTPUT           ")
print("="*50)

# Calculate Average Age and BMI safely using numpy mean
print(f"1. Average Age: {round(np.mean(df['age']), 1)} years old")
print(f"   Average BMI: {round(np.mean(df['bmi']), 1)}")
print("-"*50)

# Calculate Average Insurance Expenses for Smokers vs Non-Smokers
print("2. Average Insurance Expenses by Smoking Status:")
smoker_expenses = df.groupby('smoker')['expenses'].agg(np.mean).round(2)
print(smoker_expenses)
print("-"*50)

# Calculate Total Count of Customers in each Region
print("3. Count of Customers per Region:")
print(df['region'].value_counts())
print("==================================================\n")



