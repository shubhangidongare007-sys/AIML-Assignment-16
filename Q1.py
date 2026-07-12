import pandas as pd

df = pd.read_csv("insurance.csv",sep="\t")
print(df.head(10))