import pandas as pd
df = pd.read_csv("marks1.csv")
print(df[df["maths"] > 80])
print(df[(df["maths"] > 70) & (df["physics"] > 70)])
print(df[["name", "maths", "physics"]])
top_students = df[df["maths"] > 80]
print(top_students)
print(df.sort_values(by="maths", ascending=False))
print(df.sort_values(by=["maths", "physics"], ascending=[False, False]))
data = {
    "department": ["CS", "CS", "IT", "IT", "CS"],
    "student": ["A", "B", "C", "D", "E"],
    "marks": [85, 90, 78, 88, 92]
}
df = pd.DataFrame(data)

print(df.groupby("department")["marks"].mean())
print(df.groupby("department")["marks"].count())
print(df.groupby("department")["marks"].max())

df = pd.read_csv("marks1.csv")
print(df["physics"].mean())
print(df["maths"].mean())
print(df["chemistry"].mean())
print(df["maths"].max())

failed_students = df[(df["maths"]<=40) | (df["physics"]<=40) | (df["chemistry"]<=40)]
print(failed_students)
df_fill = df.fillna(0)
print(df_fill)
df_fill["total"] = df_fill["maths"] + df_fill["physics"] + df_fill["chemistry"]
print(df_fill.sort_values(by="total", ascending=False))

