import matplotlib.pyplot as plt
import pandas as pd

# 1. Load the dataset using the tab delimiter
df = pd.read_csv("insurance.csv", sep="\t")

# 2. Clean up any accidental hidden spaces and ensure lowercase names
df.columns = df.columns.str.strip().str.lower()

# 3. Clean the expenses data and convert it to numeric values
df["expenses"] = (
    df["expenses"].astype(str).str.replace(r"[$, ]", "", regex=True)
)
df["expenses"] = pd.to_numeric(df["expenses"], errors="coerce")

# 4. Print calculations to the terminal
print("Average Expenses:", df["expenses"].mean())
print("Maximum Expenses:", df["expenses"].max())
print("Minimum Expenses:", df["expenses"].min())

print("\nAverage Expenses by Smoker:")
smoker_gp = df.groupby("smoker")["expenses"].mean()
print(smoker_gp)

# 5. Build the bar chart layout
smoker_gp.plot(kind="bar", color=["skyblue", "salmon"])
plt.title("Average Expenses by Smoker")
plt.xlabel("Is Smoker?")
plt.ylabel("Average Expenses")
plt.xticks(rotation=0)

# 6. Display the graph window on your screen
plt.show()