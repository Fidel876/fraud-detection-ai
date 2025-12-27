import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

print("📥 Loading dataset...")
data = pd.read_csv("data/creditcard.csv")

X = data.drop("Class", axis=1)

print("⚙️ Scaling data...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("🤖 Training Isolation Forest model...")
model = IsolationForest(
    n_estimators=100,
    contamination=0.0017,
    random_state=42
)

model.fit(X_scaled)

print("💾 Saving model and scaler...")
joblib.dump(model, "model/fraud_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("✅ .pkl files created successfully")
