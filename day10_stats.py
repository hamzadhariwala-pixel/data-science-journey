import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("marks1.csv")
print("Maths mean:",df["maths"].mean())
print("Maths median:",df["maths"].median())
print("Maths mode:",df["maths"].mode())
print("Variance",df["maths"].var())
print("Std dev",df["maths"].std())
Q1= df["maths"].quantile(0.25)
Q3 = df["maths"].quantile(0.75)
IQR = Q3-Q1

outliers=df[
    (df["maths"]<Q1- 1.5*IQR)|
    (df["maths"]>Q3 + 1.5*IQR)
]
print(outliers)
plt.hist(df["maths"])
plt.axvline(df["maths"].mean())
plt.axvline(df["maths"].median())
plt.title("Maths Marks Distribution")
plt.show()