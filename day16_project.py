import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import joblib

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
# ---------------------------
model = LogisticRegression()
model.fit(X_train, y_train)

# ---------------------------
# STEP 6: Evaluate
# ---------------------------
y_pred = model.predict(X_test)

print("Train Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))
print("-" * 40)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("-" * 40)

print("Classification Report:")
print(classification_report(y_test, y_pred))

# ---------------------------
# STEP 7: Save Model
# ---------------------------
joblib.dump(model, "student_model.pkl")
print("\nModel saved as student_model.pkl")
