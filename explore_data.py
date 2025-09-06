import pandas as pd

df = pd.read_csv("data/disaster_data.csv")

print("... Dataset loaded successfully!")
print(df.head())  #shows first 5 rows

print("\nColumn names:",df.columns.tolist())

print("\nMissing values in each column:")
print(df.isnull().sum())

x = df[["rainfall","temperature","soil_moisture"]] # input features
y = df["disaster"]  # targeted input

print("\n... features and target selected!")
print(x.head())
print(y.head())

