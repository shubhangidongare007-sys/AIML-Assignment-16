import pandas as pd
df = pd.read_csv("insurance.csv",sep="\t")

# Q2
print("shape of Dataset:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary: ")
print(df.describe())