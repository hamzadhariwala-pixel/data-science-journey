import pandas as pd
df = pd.read_csv("marks1.csv")

df["total_marks"] = df["maths"] + df["physics"] + df["chemistry"]
df["avg_marks"]=df["total_marks"]/3
X = df[["maths", "physics", "chemistry"]]   # input
y = df["avg_marks"]                         # output
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.2,random_state=42
)
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)
from sklearn.metrics import mean_absolute_error, r2_score

print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))
