import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset using tab separator (\t) since your file uses tabs
df = pd.read_csv('insurance.csv', sep='\t') 

# 2. Convert all column names to lowercase to prevent naming mismatches
df.columns = df.columns.str.lower()

# 3. Create the boxplot using 'expenses' from your actual dataset column
plt.figure(figsize=(10, 6))
sns.boxplot(x='smoker', y='expenses', hue='sex', data=df, palette='Set2')

# 4. Add clean English titles and labels
plt.title('Distribution of Insurance Expenses by Smoker Status and Sex')
plt.xlabel('Smoker Status (yes / no)')
plt.ylabel('Insurance Expenses')

# 5. Display the graph window
plt.show()
