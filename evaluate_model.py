import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix

# Load data
data = pd.read_csv("data/creditcard.csv")

X = data.drop("Class", axis=1)
y = data["Class"]

# Load model & scaler
model = joblib.load("model/fraud_model.pkl")
scaler = joblib.load("model/scaler.pkl")

X_scaled = scaler.transform(X)

# Predict
preds = model.predict(X_scaled)
preds = [1 if p == -1 else 0 for p in preds]

print("Confusion Matrix:")
print(confusion_matrix(y, preds))

print("\nClassification Report:")
print(classification_report(y, preds))
