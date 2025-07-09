# Loan-Approval
This project is a Loan Approval Prediction System developed using Machine Learning and Streamlit for deployment. The goal is to automate the process of approving or rejecting loan applications based on applicant data.



> Features
Predicts loan approval status using a trained Random Forest Classifier.

Clean and user-friendly Streamlit Web App interface.

Takes inputs like income, employment status, credit history, loan amount, etc.

Displays prediction result instantly (Approved ✅ / Rejected ❌).

Option to confirm the prediction and save the result in categorized Excel files (Approved / Rejected / Confirmed).

Input validation and missing value handling included.

 > Tech Stack
Python

Scikit-learn (Random Forest Classifier)

Pandas, NumPy (Data handling)

Streamlit (Web interface)

Joblib (Model serialization)

📁 Files Included
Stored_Loan_Data.xlsx : Dataset For Training 
loan_rf_model.pkl: Trained Random Forest model.

scaler.pkl: Feature scaler for input normalization.

loanWeb.py: Main Streamlit app script.

approved.xlsx, rejected.xlsx, confirmed.xlsx: Data storage files for decisions.
