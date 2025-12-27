import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("model/fraud_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.set_page_config(page_title="Fraud Detection AI", layout="centered")
st.title("🛡️ Fraud Detection AI System")

uploaded_file = st.file_uploader("Upload transaction CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(data.head())

    # ✅ DROP Class column BEFORE scaling
    X = data.drop("Class", axis=1)

    # Scale data
    X_scaled = scaler.transform(X)

    # Predict
    predictions = model.predict(X_scaled)

    # Map results
    data["Fraud_Status"] = predictions
    data["Fraud_Status"] = data["Fraud_Status"].map({
        1: "Normal",
        -1: "Fraud"
    })

    st.subheader("Fraud Detection Results")
    st.dataframe(data[["Fraud_Status"]].value_counts())

    st.subheader("🚨 Detected Fraud Transactions")
    st.dataframe(data[data["Fraud_Status"] == "Fraud"])

