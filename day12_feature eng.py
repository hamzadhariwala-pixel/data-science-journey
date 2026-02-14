import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("marks1.csv")
df["total_marks"] = df["maths"] + df["physics"] + df["chemistry"]
df["avg_marks"]=df["total_marks"]/3
df["result"] = df["avg_marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)
def grade(x):
    if x >= 75:
        return "A"
    elif x >= 60:
        return "B"
    elif x >= 40:
        return "C"
    else:
        return "D"

df["grade"] = df["avg_marks"].apply(grade)
df["performance_level"] = pd.cut(
    df["avg_marks"],
    bins=[0, 40, 60, 75, 100],
    labels=["Poor", "Average", "Good", "Excellent"]
)
df["result_encoded"] = df["result"].map({"Fail": 0, "Pass": 1})
print(df["result"])
print(df["grade"])
print(df["performance_level"])
print(df["result_encoded"])