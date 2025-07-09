# import streamlit as st
# import pandas as pd
# import joblib

# # -----------------------------
# # Load the saved model and scaler
# # -----------------------------
# model = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_rf_model.pkl")
# scaler = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_scaler.pkl")

# # -----------------------------
# # Streamlit App
# # -----------------------------
# st.title("🏦 Loan Approval Prediction App")

# st.markdown("Fill in the details to check if the loan will be approved.")

# # Input fields
# gender = st.selectbox("Gender", ["Male", "Female"])
# married = st.selectbox("Married", ["Yes", "No"])
# education = st.selectbox("Education", ["Graduate", "Not Graduate"])
# self_employed = st.selectbox("Self Employed", ["Yes", "No"])
# applicant_income = st.number_input("Applicant Income", min_value=0)
# coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
# loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
# loan_amount_term = st.selectbox("Loan Term (in days)", [360.0, 180.0, 120.0, 84.0, 60.0])
# credit_history = st.selectbox("Credit History (1 = good, 0 = bad)", [1, 0])
# dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
# property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# # Predict button
# if st.button("Check Loan Approval"):
#     # Create DataFrame for prediction
#     input_data = pd.DataFrame({
#         'Gender': [1 if gender == 'Male' else 0],
#         'Married': [1 if married == 'Yes' else 0],
#         'Education': [1 if education == 'Graduate' else 0],
#         'Self_Employed': [1 if self_employed == 'Yes' else 0],
#         'ApplicantIncome': [applicant_income],
#         'CoapplicantIncome': [coapplicant_income],
#         'LoanAmount': [loan_amount],
#         'Loan_Amount_Term': [loan_amount_term],
#         'Credit_History': [credit_history],
#         'Dependents_1': [1 if dependents == '1' else 0],
#         'Dependents_2': [1 if dependents == '2' else 0],
#         'Dependents_3+': [1 if dependents == '3+' else 0],
#         'Property_Area_Semiurban': [1 if property_area == 'Semiurban' else 0],
#         'Property_Area_Urban': [1 if property_area == 'Urban' else 0],
#     })

#     # Scale numerical features
#     input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']] = scaler.transform(
#         input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']]
#     )

#     # Predict
#     prediction = model.predict(input_data)[0]

#     # Output
#     if prediction == 1:
#         st.success("✅ Loan is likely to be Approved!")
#     else:
#         st.error("❌ Loan is likely to be Rejected.")


# loanWeb.py

# import streamlit as st
# import pandas as pd
# import joblib

# # Load the saved model and scaler
# model = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_rf_model.pkl")  # Make sure this path is correct
# scaler = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_scaler.pkl")

# st.title("🏦 Loan Approval Prediction App")
# st.markdown("Fill in the details to check if the loan will be approved.")

# # Input fields
# gender = st.selectbox("Gender", ["Male", "Female"])
# married = st.selectbox("Married", ["Yes", "No"])
# education = st.selectbox("Education", ["Graduate", "Not Graduate"])
# self_employed = st.selectbox("Self Employed", ["Yes", "No"])
# applicant_income = st.number_input("Applicant Income", min_value=0)
# coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
# loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
# loan_amount_term = st.selectbox("Loan Term (in days)", [360.0, 180.0, 120.0, 84.0, 60.0])
# credit_history = st.selectbox("Credit History (1 = good, 0 = bad)", [1, 0])
# dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
# property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# # Predict button
# if st.button("Check Loan Approval"):
#     # Create DataFrame for prediction
#     input_data = pd.DataFrame({
#         'Gender': [1 if gender == 'Male' else 0],
#         'Married': [1 if married == 'Yes' else 0],
#         'Education': [1 if education == 'Graduate' else 0],
#         'Self_Employed': [1 if self_employed == 'Yes' else 0],
#         'ApplicantIncome': [applicant_income],
#         'CoapplicantIncome': [coapplicant_income],
#         'LoanAmount': [loan_amount],
#         'Loan_Amount_Term': [loan_amount_term],
#         'Credit_History': [credit_history],
#         'Dependents_1': [1 if dependents == '1' else 0],
#         'Dependents_2': [1 if dependents == '2' else 0],
#         'Dependents_3+': [1 if dependents == '3+' else 0],
#         'Property_Area_Semiurban': [1 if property_area == 'Semiurban' else 0],
#         'Property_Area_Urban': [1 if property_area == 'Urban' else 0],
#     })

#     # Scale numerical features
#     input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']] = scaler.transform(
#         input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']]
#     )

#     # Make prediction
#     try:
#         prediction = model.predict(input_data)[0]
#         if prediction == 1:
#             st.success("✅ Loan is likely to be Approved!")
#         else:
#             st.error("❌ Loan is likely to be Rejected.")
#     except Exception as e:
#         st.error(f"🚫 Prediction failed: {str(e)}")

# import streamlit as st
# import pandas as pd
# import joblib
# import os

# # -----------------------------
# # Load model and scaler
# # -----------------------------
# model = joblib.load("loan_rf_model.pkl")  # Update path if needed
# scaler = joblib.load("loan_scaler.pkl")

# st.title("🏦 Loan Approval Prediction App")

# st.markdown("### Enter Loan Applicant Details")

# # ➤ Additional fields
# name = st.text_input("Full Name")
# age = st.number_input("Age", min_value=18, max_value=100)

# # ➤ Main input fields
# gender = st.selectbox("Gender", ["Male", "Female"])
# married = st.selectbox("Married", ["Yes", "No"])
# education = st.selectbox("Education", ["Graduate", "Not Graduate"])
# self_employed = st.selectbox("Self Employed", ["Yes", "No"])
# applicant_income = st.number_input("Applicant Income", min_value=0)
# coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
# loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
# loan_amount_term = st.selectbox("Loan Term (in days)", [360.0, 180.0, 120.0, 84.0, 60.0])
# credit_history = st.selectbox("Credit History (1 = Good, 0 = Bad)", [1, 0])
# dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
# property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# # ➤ Prediction
# if st.button("Check Loan Approval"):

#     # ➤ Convert inputs to model-ready format
#     input_data = pd.DataFrame([{
#         'Gender': 1 if gender == 'Male' else 0,
#         'Married': 1 if married == 'Yes' else 0,
#         'Education': 1 if education == 'Graduate' else 0,
#         'Self_Employed': 1 if self_employed == 'Yes' else 0,
#         'ApplicantIncome': applicant_income,
#         'CoapplicantIncome': coapplicant_income,
#         'LoanAmount': loan_amount,
#         'Loan_Amount_Term': loan_amount_term,
#         'Credit_History': credit_history,
#         'Dependents_1': 1 if dependents == '1' else 0,
#         'Dependents_2': 1 if dependents == '2' else 0,
#         'Dependents_3+': 1 if dependents in ['3', '3+'] else 0,
#         'Property_Area_Semiurban': 1 if property_area == 'Semiurban' else 0,
#         'Property_Area_Urban': 1 if property_area == 'Urban' else 0
#     }])

#     # ➤ Scale
#     input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']] = scaler.transform(
#         input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']]
#     )

#     # ➤ Predict
#     result = model.predict(input_data)[0]

#     # ➤ Show result
#     if result == 1:
#         st.success("✅ Loan is likely to be Approved!")
#     else:
#         st.error("❌ Loan is likely to be Rejected.")

#     # ➤ Save user data
#     original_data = input_data.copy()
#     original_data.insert(0, "Name", name)
#     original_data.insert(1, "Age", age)
#     original_data['Loan_Status'] = 'Approved' if result == 1 else 'Rejected'

#     # ➤ Save to all applications
#     all_path = "all_loans.csv"
#     if os.path.exists(all_path):
#         existing = pd.read_csv(all_path)
#         updated = pd.concat([existing, original_data], ignore_index=True)
#         updated.to_csv(all_path, index=False)
#     else:
#         original_data.to_csv(all_path, index=False)

#     # ➤ Save to rejected list
#     if result == 0:
#         reject_path = "rejected_loans.csv"
#         if os.path.exists(reject_path):
#             existing = pd.read_csv(reject_path)
#             updated = pd.concat([existing, original_data], ignore_index=True)
#             updated.to_csv(reject_path, index=False)
#         else:
#             original_data.to_csv(reject_path, index=False)

# import streamlit as st
# import pandas as pd
# import joblib
# import os

# # -----------------------------
# # Load model and scaler
# # -----------------------------
# model = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_rf_model.pkl")
# scaler = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_scaler.pkl")

# st.title("🏦 Loan Approval Prediction App")
# st.markdown("### Enter Loan Applicant Details")

# # ➤ File paths (same folder as script)
# confirmed_file = r"C:\Users\Home\Desktop\Python\AI Internship\project\confirmed_loans.xlsx"
# approved_file = r"C:\Users\Home\Desktop\Python\AI Internship\project\approved_loans.xlsx"
# rejected_file = r"C:\Users\Home\Desktop\Python\AI Internship\project\rejected_loans.xlsx"

# # ➤ Ensure files exist
# for file in [confirmed_file, approved_file, rejected_file]:
#     if not os.path.exists(file):
#         df_init = pd.DataFrame(columns=["Name", "Age", "Loan_Status"])  # Start with empty
#         df_init.to_excel(file, index=False)

# # ➤ Input fields
# name = st.text_input("Full Name")
# age = st.number_input("Age", min_value=18, max_value=100)
# gender = st.selectbox("Gender", ["Male", "Female"])
# married = st.selectbox("Married", ["Yes", "No"])
# education = st.selectbox("Education", ["Graduate", "Not Graduate"])
# self_employed = st.selectbox("Self Employed", ["Yes", "No"])
# applicant_income = st.number_input("Applicant Income", min_value=0)
# coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
# loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
# loan_amount_term = st.selectbox("Loan Term (in days)", [360.0, 180.0, 120.0, 84.0, 60.0])
# credit_history = st.selectbox("Credit History (1 = Good, 0 = Bad)", [1, 0])
# dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
# property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# # ➤ Prediction
# if st.button("Check Loan Approval"):
#     input_data = pd.DataFrame([{
#         'Gender': 1 if gender == 'Male' else 0,
#         'Married': 1 if married == 'Yes' else 0,
#         'Education': 1 if education == 'Graduate' else 0,
#         'Self_Employed': 1 if self_employed == 'Yes' else 0,
#         'ApplicantIncome': applicant_income,
#         'CoapplicantIncome': coapplicant_income,
#         'LoanAmount': loan_amount,
#         'Loan_Amount_Term': loan_amount_term,
#         'Credit_History': credit_history,
#         'Dependents_1': 1 if dependents == '1' else 0,
#         'Dependents_2': 1 if dependents == '2' else 0,
#         'Dependents_3+': 1 if dependents in ['3', '3+'] else 0,
#         'Property_Area_Semiurban': 1 if property_area == 'Semiurban' else 0,
#         'Property_Area_Urban': 1 if property_area == 'Urban' else 0
#     }])

#     # ➤ Scale
#     input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']] = scaler.transform(
#         input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']]
#     )

#     # ➤ Predict
#     result = model.predict(input_data)[0]

#     # ➤ Display result
#     st.markdown("---")
#     if result == 1:
#         st.success("✅ Loan is likely to be Approved!")
#     else:
#         st.error("❌ Loan is likely to be Rejected.")

#     # ➤ Ask for confirmation
#     confirm = st.radio("Do you want to confirm and save this application?", ["No", "Yes"], index=0)

#     if confirm == "Yes":
#         # ➤ Prepare full row
#         final_data = input_data.copy()
#         final_data.insert(0, "Name", name)
#         final_data.insert(1, "Age", age)
#         final_data['Loan_Status'] = 'Approved' if result == 1 else 'Rejected'

#         # ➤ Append to confirmed
#         df_c = pd.read_excel(confirmed_file)
#         df_c = pd.concat([df_c, final_data], ignore_index=True)
#         df_c.to_excel(confirmed_file, index=False)

#         # ➤ Append to approved or rejected
#         if result == 1:
#             df_a = pd.read_excel(approved_file)
#             df_a = pd.concat([df_a, final_data], ignore_index=True)
#             df_a.to_excel(approved_file, index=False)
#         else:
#             df_r = pd.read_excel(rejected_file)
#             df_r = pd.concat([df_r, final_data], ignore_index=True)
#             df_r.to_excel(rejected_file, index=False)

#         st.success("✅ Application saved successfully!")

# # ➤ View all saved files
# # ➤ View files section with buttons
# st.markdown("### 📂 View Saved Loan Applications")

# if st.button("📄 View Confirmed Loans"):
#     if os.path.exists(confirmed_file):
#         df_view = pd.read_excel(confirmed_file)
#         st.subheader("✅ Confirmed Loans")
#         st.dataframe(df_view)
#     else:
#         st.warning("Confirmed loans file not found.")

# if st.button("📄 View Approved Loans"):
#     if os.path.exists(approved_file):
#         df_view = pd.read_excel(approved_file)
#         st.subheader("🟢 Approved Loans")
#         st.dataframe(df_view)
#     else:
#         st.warning("Approved loans file not found.")

# if st.button("📄 View Rejected Loans"):
#     if os.path.exists(rejected_file):
#         df_view = pd.read_excel(rejected_file)
#         st.subheader("🔴 Rejected Loans")
#         st.dataframe(df_view)
#     else:
#         st.warning("!Rejected loans file not found.")

# import streamlit as st
# import pandas as pd
# import joblib
# import os

# # -----------------------------
# # Load model and scaler
# # -----------------------------
# model = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_rf_model.pkl")
# scaler = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_scaler.pkl")

# st.title("🏦 Loan Approval Prediction App")
# st.markdown("### Enter Loan Applicant Details")

# # ➤ File paths (stored in same folder as script)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# confirmed_file = os.path.join(BASE_DIR, "confirmed_loans.xlsx")
# approved_file = os.path.join(BASE_DIR, "approved_loans.xlsx")
# rejected_file = os.path.join(BASE_DIR, "rejected_loans.xlsx")

# # ➤ Ensure Excel files exist
# for file in [confirmed_file, approved_file, rejected_file]:
#     if not os.path.exists(file):
#         df_init = pd.DataFrame(columns=["Name", "Age", "Loan_Status"])
#         df_init.to_excel(file, index=False)

# # ➤ User Input
# name = st.text_input("Full Name")
# age = st.number_input("Age", min_value=18, max_value=100)
# gender = st.selectbox("Gender", ["Male", "Female"])
# married = st.selectbox("Married", ["Yes", "No"])
# education = st.selectbox("Education", ["Graduate", "Not Graduate"])
# self_employed = st.selectbox("Self Employed", ["Yes", "No"])
# applicant_income = st.number_input("Applicant Income", min_value=0)
# coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
# loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
# loan_amount_term = st.selectbox("Loan Term (in days)", [360.0, 180.0, 120.0, 84.0, 60.0])
# credit_history = st.selectbox("Credit History (1 = Good, 0 = Bad)", [1, 0])
# dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
# property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# # ➤ Prediction logic
# if st.button("Check Loan Approval"):
#     input_data = pd.DataFrame([{
#         'Gender': 1 if gender == 'Male' else 0,
#         'Married': 1 if married == 'Yes' else 0,
#         'Education': 1 if education == 'Graduate' else 0,
#         'Self_Employed': 1 if self_employed == 'Yes' else 0,
#         'ApplicantIncome': applicant_income,
#         'CoapplicantIncome': coapplicant_income,
#         'LoanAmount': loan_amount,
#         'Loan_Amount_Term': loan_amount_term,
#         'Credit_History': credit_history,
#         'Dependents_1': 1 if dependents == '1' else 0,
#         'Dependents_2': 1 if dependents == '2' else 0,
#         'Dependents_3+': 1 if dependents in ['3', '3+'] else 0,
#         'Property_Area_Semiurban': 1 if property_area == 'Semiurban' else 0,
#         'Property_Area_Urban': 1 if property_area == 'Urban' else 0
#     }])

#     # ➤ Scale selected numeric columns
#     input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']] = scaler.transform(
#         input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']]
#     )

#     # ➤ Predict loan status
#     result = model.predict(input_data)[0]
#     loan_status = "Approved" if result == 1 else "Rejected"

#     # ➤ Create full data with extra fields
#     full_data = input_data.copy()
#     full_data.insert(0, "Name", name)
#     full_data.insert(1, "Age", age)
#     full_data["Loan_Status"] = loan_status

#     st.markdown("---")

#     if result == 1:
#         st.success("✅ Loan is likely to be Approved!")

#         # Save to approved file
#         df_approved = pd.read_excel(approved_file)
#         df_approved = pd.concat([df_approved, full_data], ignore_index=True)
#         df_approved.to_excel(approved_file, index=False)

#         # Ask for confirmation (with no default selected)
#         confirm = st.selectbox("Do you confirm this approval?", ["Select an option", "Yes", "No"])
#         if confirm == "Yes":
#             df_confirmed = pd.read_excel(confirmed_file)
#             df_confirmed = pd.concat([df_confirmed, full_data], ignore_index=True)
#             df_confirmed.to_excel(confirmed_file, index=False)
#             st.success("✅ Saved to Confirmed.")
#         elif confirm == "No":
#             df_rejected = pd.read_excel(rejected_file)
#             df_rejected = pd.concat([df_rejected, full_data], ignore_index=True)
#             df_rejected.to_excel(rejected_file, index=False)
#             st.info("❌ Moved to Rejected.")
#     else:
#         st.error("❌ Loan is likely to be Rejected.")
#         df_rejected = pd.read_excel(rejected_file)
#         df_rejected = pd.concat([df_rejected, full_data], ignore_index=True)
#         df_rejected.to_excel(rejected_file, index=False)

# # ➤ Display saved data
# st.markdown("## 📂 View Saved Applications")
# for file in [confirmed_file, approved_file, rejected_file]:
#     file_label = os.path.basename(file)
#     if os.path.exists(file):
#         st.subheader(f"📁 {file_label}")
#         df_view = pd.read_excel(file)
#         st.dataframe(df_view)
#     else:
#         st.warning(f"⚠️ File not found: {file_label}")

# import streamlit as st
# import pandas as pd
# import joblib
# import os

# # -----------------------------
# # Load model and scaler
# # -----------------------------
# model = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_rf_model.pkl")
# scaler = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_scaler.pkl")

# st.title("🏦 Loan Approval Prediction App")
# st.markdown("### Enter Loan Applicant Details")

# # ➤ File paths (same folder as script)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# confirmed_file = os.path.join(BASE_DIR, "confirmed_loans.xlsx")
# approved_file = os.path.join(BASE_DIR, "approved_loans.xlsx")
# rejected_file = os.path.join(BASE_DIR, "rejected_loans.xlsx")

# # ➤ Ensure files exist
# for file in [confirmed_file, approved_file, rejected_file]:
#     if not os.path.exists(file):
#         pd.DataFrame(columns=["Name", "Age", "Loan_Status"]).to_excel(file, index=False)

# # ➤ Input fields
# name = st.text_input("Full Name")
# age = st.number_input("Age", min_value=18, max_value=100)
# gender = st.selectbox("Gender", ["Male", "Female"])
# married = st.selectbox("Married", ["Yes", "No"])
# education = st.selectbox("Education", ["Graduate", "Not Graduate"])
# self_employed = st.selectbox("Self Employed", ["Yes", "No"])
# applicant_income = st.number_input("Applicant Income", min_value=0)
# coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
# loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
# loan_amount_term = st.selectbox("Loan Term (in days)", [360.0, 180.0, 120.0, 84.0, 60.0])
# credit_history = st.selectbox("Credit History (1 = Good, 0 = Bad)", [1, 0])
# dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
# property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# # ➤ Initialize session state
# if "result" not in st.session_state:
#     st.session_state.result = None
# if "full_data" not in st.session_state:
#     st.session_state.full_data = None
# if "prediction_done" not in st.session_state:
#     st.session_state.prediction_done = False

# # ➤ Prediction
# if st.button("Check Loan Approval"):
#     input_data = pd.DataFrame([{
#         'Gender': 1 if gender == 'Male' else 0,
#         'Married': 1 if married == 'Yes' else 0,
#         'Education': 1 if education == 'Graduate' else 0,
#         'Self_Employed': 1 if self_employed == 'Yes' else 0,
#         'ApplicantIncome': applicant_income,
#         'CoapplicantIncome': coapplicant_income,
#         'LoanAmount': loan_amount,
#         'Loan_Amount_Term': loan_amount_term,
#         'Credit_History': credit_history,
#         'Dependents_1': 1 if dependents == '1' else 0,
#         'Dependents_2': 1 if dependents == '2' else 0,
#         'Dependents_3+': 1 if dependents in ['3', '3+'] else 0,
#         'Property_Area_Semiurban': 1 if property_area == 'Semiurban' else 0,
#         'Property_Area_Urban': 1 if property_area == 'Urban' else 0
#     }])

#     input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']] = scaler.transform(
#         input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']]
#     )

#     result = model.predict(input_data)[0]
#     loan_status = "Approved" if result == 1 else "Rejected"

#     full_data = input_data.copy()
#     full_data.insert(0, "Name", name)
#     full_data.insert(1, "Age", age)
#     full_data["Loan_Status"] = loan_status

#     # Save result and data to session state
#     st.session_state.result = result
#     st.session_state.full_data = full_data
#     st.session_state.prediction_done = True

# # ➤ Show Result if prediction was done
# if st.session_state.prediction_done:
#     result = st.session_state.result
#     full_data = st.session_state.full_data

#     st.markdown("---")
#     if result == 1:
#         st.success("✅ Loan is likely to be Approved!")

#         # Save to approved immediately
#         df_approved = pd.read_excel(approved_file)
#         df_approved = pd.concat([df_approved, full_data], ignore_index=True)
#         df_approved.to_excel(approved_file, index=False)

#         confirm = st.selectbox("Do you confirm this approval?", ["Select an option", "Yes", "No"])

#         if confirm == "Yes":
#             df_confirmed = pd.read_excel(confirmed_file)
#             df_confirmed = pd.concat([df_confirmed, full_data], ignore_index=True)
#             df_confirmed.to_excel(confirmed_file, index=False)
#             st.success("✅ Saved to Confirmed.")

#         elif confirm == "No":
#             df_rejected = pd.read_excel(rejected_file)
#             df_rejected = pd.concat([df_rejected, full_data], ignore_index=True)
#             df_rejected.to_excel(rejected_file, index=False)
#             st.info("❌ Moved to Rejected.")

#     else:
#         st.error("❌ Loan is likely to be Rejected.")
#         df_rejected = pd.read_excel(rejected_file)
#         df_rejected = pd.concat([df_rejected, full_data], ignore_index=True)
#         df_rejected.to_excel(rejected_file, index=False)

#     # Reset prediction flag
#     st.session_state.prediction_done = False

# # ➤ View all saved files
# st.markdown("### 📄 View Saved Loan Applications")
# for file in [confirmed_file, approved_file, rejected_file]:
#     file_label = os.path.basename(file)
#     if os.path.exists(file):
#         st.subheader(f"📁 {file_label}")
#         df_show = pd.read_excel(file)
#         st.dataframe(df_show)
#     else:
#         st.warning(f"❗ {file_label} not found.")


# import streamlit as st
# import pandas as pd
# import joblib
# import os

# # -----------------------------
# # Load model and scaler
# # -----------------------------
# model = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_rf_model.pkl")
# scaler = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_scaler.pkl")

# st.title("🏦 Loan Approval Prediction App")
# st.markdown("### Enter Loan Applicant Details")

# # -----------------------------
# # File Paths
# # -----------------------------
# BASE_DIR = r"C:\Users\Home\Desktop\Python\AI Internship\project"
# confirmed_file = os.path.join(BASE_DIR, "confirmed_loans.xlsx")
# approved_file = os.path.join(BASE_DIR, "approved_loans.xlsx")
# rejected_file = os.path.join(BASE_DIR, "rejected_loans.xlsx")

# # -----------------------------
# # Create Excel files if not exist
# # -----------------------------
# for file in [confirmed_file, approved_file, rejected_file]:
#     if not os.path.exists(file):
#         pd.DataFrame(columns=["Name", "Age", "Loan_Status"]).to_excel(file, index=False)

# # -----------------------------
# # Input Fields
# # -----------------------------
# name = st.text_input("Full Name")
# age = st.number_input("Age", min_value=18, max_value=100)
# gender = st.selectbox("Gender", ["Male", "Female"])
# married = st.selectbox("Married", ["Yes", "No"])
# education = st.selectbox("Education", ["Graduate", "Not Graduate"])
# self_employed = st.selectbox("Self Employed", ["Yes", "No"])
# applicant_income = st.number_input("Applicant Income", min_value=0)
# coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
# loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
# loan_amount_term = st.selectbox("Loan Term (in days)", [360.0, 180.0, 120.0, 84.0, 60.0])
# credit_history = st.selectbox("Credit History (1 = Good, 0 = Bad)", [1, 0])
# dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
# property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# # -----------------------------
# # Prediction
# # -----------------------------
# if st.button("Check Loan Approval"):
#     input_data = pd.DataFrame([{
#         'Gender': 1 if gender == 'Male' else 0,
#         'Married': 1 if married == 'Yes' else 0,
#         'Education': 1 if education == 'Graduate' else 0,
#         'Self_Employed': 1 if self_employed == 'Yes' else 0,
#         'ApplicantIncome': applicant_income,
#         'CoapplicantIncome': coapplicant_income,
#         'LoanAmount': loan_amount,
#         'Loan_Amount_Term': loan_amount_term,
#         'Credit_History': credit_history,
#         'Dependents_1': 1 if dependents == '1' else 0,
#         'Dependents_2': 1 if dependents == '2' else 0,
#         'Dependents_3+': 1 if dependents in ['3', '3+'] else 0,
#         'Property_Area_Semiurban': 1 if property_area == 'Semiurban' else 0,
#         'Property_Area_Urban': 1 if property_area == 'Urban' else 0
#     }])

#     input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']] = scaler.transform(
#         input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']]
#     )

#     result = model.predict(input_data)[0]

#     # Prepare full data row
#     full_data = input_data.copy()
#     full_data.insert(0, "Name", name)
#     full_data.insert(1, "Age", age)
#     full_data["Loan_Status"] = "Approved" if result == 1 else "Rejected"

#     st.markdown("---")

#     # Approved Case
#     if result == 1:
#         st.success("✅ Loan is likely to be Approved!")

#         # Save to approved
#         df_a = pd.read_excel(approved_file)
#         df_a = pd.concat([df_a, full_data], ignore_index=True)
#         df_a.to_excel(approved_file, index=False)

#         # Ask for confirmation with no default selected
#         confirm = st.radio("Do you confirm this approval?", ["Yes", "No"], index=None)

#         if confirm == "Yes":
#             df_c = pd.read_excel(confirmed_file)
#             df_c = pd.concat([df_c, full_data], ignore_index=True)
#             df_c.to_excel(confirmed_file, index=False)
#             st.success("✅ Saved to Confirmed File.")
#         elif confirm == "No":
#             df_r = pd.read_excel(rejected_file)
#             df_r = pd.concat([df_r, full_data], ignore_index=True)
#             df_r.to_excel(rejected_file, index=False)
#             st.warning("❌ Moved to Rejected File.")

#     # Rejected Case
#     else:
#         st.error("❌ Loan is likely to be Rejected.")
#         df_r = pd.read_excel(rejected_file)
#         df_r = pd.concat([df_r, full_data], ignore_index=True)
#         df_r.to_excel(rejected_file, index=False)

# # -----------------------------
# # View Saved Files
# # -----------------------------
# st.markdown("### 📄 View Saved Applications")

# for file in [confirmed_file, approved_file, rejected_file]:
#     label = os.path.basename(file)
#     if os.path.exists(file):
#         st.subheader(f"📁 {label}")
#         try:
#             df_show = pd.read_excel(file)
#             st.dataframe(df_show)
#         except Exception as e:
#             st.error(f"Could not read {label}: {e}")


import streamlit as st
import pandas as pd
import joblib
import os

# Load model and scaler
model = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_rf_model.pkl")
scaler = joblib.load(r"C:\Users\Home\Desktop\Python\AI Internship\project\loan_scaler.pkl")

st.title("🏦 Loan Approval Prediction App")
st.markdown("### Enter Loan Applicant Details")

# Set paths to Excel files
base_dir = r"C:\Users\Home\Desktop\Python\AI Internship\project"
confirmed_file = os.path.join(base_dir, "confirmed_loans.xlsx")
approved_file = os.path.join(base_dir, "approved_loans.xlsx")
rejected_file = os.path.join(base_dir, "rejected_loans.xlsx")

# Create files if they don’t exist
for file in [confirmed_file, approved_file, rejected_file]:
    if not os.path.exists(file):
        pd.DataFrame(columns=["Name", "Age", "Loan_Status"]).to_excel(file, index=False)

# Input fields
name = st.text_input("Full Name")
age = st.number_input("Age", min_value=18, max_value=100)
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_amount_term = st.selectbox("Loan Term (in days)", [360.0, 180.0, 120.0, 84.0, 60.0])
credit_history = st.selectbox("Credit History (1 = Good, 0 = Bad)", [1, 0])
dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Prediction
if st.button("Check Loan Approval"):
    input_data = pd.DataFrame([{
        'Gender': 1 if gender == 'Male' else 0,
        'Married': 1 if married == 'Yes' else 0,
        'Education': 1 if education == 'Graduate' else 0,
        'Self_Employed': 1 if self_employed == 'Yes' else 0,
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_amount_term,
        'Credit_History': credit_history,
        'Dependents_1': 1 if dependents == '1' else 0,
        'Dependents_2': 1 if dependents == '2' else 0,
        'Dependents_3+': 1 if dependents in ['3', '3+'] else 0,
        'Property_Area_Semiurban': 1 if property_area == 'Semiurban' else 0,
        'Property_Area_Urban': 1 if property_area == 'Urban' else 0
    }])

    # Scale numeric values
    input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']] = scaler.transform(
        input_data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']]
    )

    result = model.predict(input_data)[0]

    # Add metadata
    full_data = input_data.copy()
    full_data.insert(0, "Name", name)
    full_data.insert(1, "Age", age)
    full_data["Loan_Status"] = "Approved" if result == 1 else "Rejected"

    st.markdown("---")

    if result == 1:
        st.success("✅ Loan is likely to be Approved!")

        # Save to approved
        df_a = pd.read_excel(approved_file)
        df_a = pd.concat([df_a, full_data], ignore_index=True)
        df_a.to_excel(approved_file, index=False)

        # Ask for confirmation (no default)
        confirm = st.radio("Do you confirm this approval?", ["Yes", "No"], index=None)

        if confirm == "Yes":
            df_c = pd.read_excel(confirmed_file)
            df_c = pd.concat([df_c, full_data], ignore_index=True)
            df_c.to_excel(confirmed_file, index=False)
            st.success("✅ Saved to Confirmed.")
        elif confirm == "No":
            df_r = pd.read_excel(rejected_file)
            df_r = pd.concat([df_r, full_data], ignore_index=True)
            df_r.to_excel(rejected_file, index=False)
            st.info("❌ Moved to Rejected.")

    else:
        st.error("❌ Loan is likely to be Rejected.")
        df_r = pd.read_excel(rejected_file)
        df_r = pd.concat([df_r, full_data], ignore_index=True)
        df_r.to_excel(rejected_file, index=False)

# View Files
st.markdown("### 📄 View Saved Loan Applications")
for file in [confirmed_file, approved_file, rejected_file]:
    label = os.path.basename(file)
    st.subheader(f"📁 {label}")
    try:
        df_view = pd.read_excel(file)
        st.dataframe(df_view)
    except Exception as e:
        st.warning(f"⚠️ Couldn't load {label}: {e}")
