
🛡 FRAUD DETECTION AI — CREDIT CARD TRANSACTION ANALYSIS

# Project Summary
This project detects suspicious or potentially fraudulent credit-card transactions using anomaly detection. Instead of treating fraud as a normal classification problem, I used the Isolation Forest algorithm to identify unusual transaction patterns in a highly imbalanced dataset. The objective was to understand how fraud detection systems work in practice and to build an end-to-end workflow from preprocessing the data to generating predictions through a simple web application.

# Approach & Model
• Technique: Isolation Forest (Unsupervised Anomaly Detection)
• Reason: Fraud cases are rare and dataset is highly imbalanced
• Features are scaled using StandardScaler
• Model and scaler are saved as .pkl files for reuse in the app

# What the Project Does
• Loads and preprocesses transaction data
• Flags abnormal / suspicious transactions
• Evaluates how well fraud cases are detected
• Streamlit web app for CSV upload and prediction
• Displays summary of detected fraud cases

# Tools & Libraries
Python | Pandas | NumPy | Scikit-Learn | Isolation Forest | Streamlit | Joblib

# Dataset
Credit Card Fraud Detection Dataset (Kaggle)
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
(Note: Dataset not included in repo due to size limits — place inside data/ folder)

# How to Run
pip install -r requirements.txt
python train_model.py
streamlit run app.py

# Key Files
train_model.py — trains Isolation Forest model
evaluate_model.py — evaluates model performance
app.py — Streamlit prediction app
model/ — saved model + scaler files
data/ — dataset folder (ignored in repo)

# Learning Outcomes
• Worked with highly imbalanced datasets
• Understood anomaly detection vs classification
• Built an end-to-end ML workflow
• Implemented model saving & reuse with Joblib
• Created a simple ML web application using Streamlit
