import pandas as pd
df = pd.read_csv("marks1.csv")

df["total_marks"] = df["maths"] + df["physics"] + df["chemistry"]
df["avg_marks"]=df["total_marks"]/3

df["result"] = df["avg_marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)
df["result_encoded"] = df["result"].map({"Fail": 0, "Pass": 1})
X = df[["maths", "physics", "chemistry"]]
y = df["result_encoded"]
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Report:\n", classification_report(y_test, y_pred))
print("Train Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))
print(classification_report(y_test, y_pred))
