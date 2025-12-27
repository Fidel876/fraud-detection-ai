🛡️ FRAUD DETECTION AI SYSTEM — ONE SLIDE SUMMARY

📌 Description  
An AI-based fraud detection system that identifies anomalous financial transactions using Isolation Forest.  
Built end-to-end with data preprocessing, feature scaling, model training, evaluation, and a Streamlit web app for real-time CSV-based prediction.

🧠 Machine Learning  
• Technique: Isolation Forest (Unsupervised Anomaly Detection)  
• Handles highly imbalanced datasets  
• Evaluation: Recall, Precision, F1-Score, Confusion Matrix  

🛠 Tech Stack  
Python | Pandas | NumPy | Scikit-Learn | Isolation Forest | Streamlit | Joblib

🚀 Features  
• Detects suspicious / fraudulent transactions  
• Scales features using StandardScaler  
• Upload CSV → Predict fraud in real-time  
• Displays fraud summary & flagged records

📂 Dataset  
Credit Card Fraud Detection Dataset — Kaggle  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud  
(Note: Dataset not included in repo due to size — place it inside /data/)

📁 Project Structure  
• train_model.py — trains model & saves .pkl files  
• evaluate_model.py — model evaluation  
• app.py — Streamlit fraud detection app  
• model/ — saved model files  
• data/ — dataset folder (ignored in repo)

▶️ How to Run  
pip install -r requirements.txt  
python train_model.py  
streamlit run app.py

🎯 Outcome / Learning  
• Gained experience in anomaly detection & imbalanced data  
• Built an end-to-end ML workflow  
• Implemented real-time ML app using Streamlit
