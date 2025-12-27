# Fraud Detection AI System

An AI-based system to detect fraudulent financial transactions using anomaly detection.

## Tech Stack
- Python
- Scikit-learn
- Streamlit
- Isolation Forest

## Features
- Detects anomalous transactions
- Handles highly imbalanced data
- Web-based interface for real-time analysis

## Model
- Isolation Forest (unsupervised learning)

## Dataset
- This project uses the **Credit Card Fraud Detection Dataset** from Kaggle.

- Dataset link:
  https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

> Note: The dataset is not included in this repository because it is large.
> Download it from Kaggle and place it inside the `data/` folder before running the project.
)

## How to Run
pip install -r requirements.txt
python train_model.py
streamlit run app.py
