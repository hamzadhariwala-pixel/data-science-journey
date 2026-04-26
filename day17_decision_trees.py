import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

# ---------------------------
# STEP 1: Load Data
# ---------------------------
df = pd.read_csv("student_project.csv")

# ---------------------------
# STEP 2: Feature Engineering
# ---------------------------
df["avg_marks"] = df[["maths", "physics", "chemistry"]].mean(axis=1)

# Pass if avg >= 50 AND attendance >= 60
df["result"] = df.apply(
    lambda row: "Pass" if row["avg_marks"] >= 50 and row["attendance"] >= 60 else "Fail",
    axis=1
)

df["result_encoded"] = df["result"].map({"Fail": 0, "Pass": 1})

print("Class Distribution:")
print(df["result_encoded"].value_counts())
print("-" * 40)

# ---------------------------
# STEP 3: Define Features
# ---------------------------
X = df[["maths", "physics", "chemistry", "attendance"]]
y = df["result_encoded"]

# ---------------------------
# STEP 4: Split
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# ---------------------------
# STEP 5: Train Model

model = LogisticRegression()
model.fit(X_train, y_train)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
print("Train Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))
scores = cross_val_score(model, X, y, cv=5)

print("All scores:", scores)
print("Average accuracy:", scores.mean())
