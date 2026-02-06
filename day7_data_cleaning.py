import pandas as pd

df = pd.read_csv("marks1.csv")
print(df)
print(df.isnull())
print(df.isnull().sum())

df["physics"] = df["physics"].fillna(df["physics"].mean())
df["chemistry"] = df["chemistry"].fillna(df["chemistry"].mean())
df["maths"] = df["maths"].fillna(df["maths"].mean())
print(df.dtypes)
df["maths"] = df["maths"].astype(int)
df["name"] = df["name"].str.strip()
df["name"] = df["name"].str.lower()
print(df)
