import pandas as pd

df =  pd.read_csv("insurance.csv",sep="\t")

print("Missing Values: ")
print(df.isnull().sum())