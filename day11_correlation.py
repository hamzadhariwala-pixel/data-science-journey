import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("marks1.csv")
print(df["maths"].corr(df["physics"]))
print(df["maths"].corr(df["chemistry"]))
df_fill=df.fillna(0)
corr_matrix=df_fill.corr()
print(corr_matrix)
plt.scatter(df["maths"],df["physics"])
plt.xlabel("Maths")
plt.ylabel("Physics")
plt.title("Maths vs Physics")
plt.show()
