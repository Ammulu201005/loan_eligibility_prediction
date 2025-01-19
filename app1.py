import streamlit as st
import pickle
import numpy as np

# Load the model
with open('loan_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app
st.title("Loan Approval Prediction")

# Input fields for user
applicant_income = st.number_input("Applicant Income", min_value=0, value=5000)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0, value=2000)
loan_amount = st.number_input("Loan Amount", min_value=0, value=100)
credit_history = st.selectbox("Credit History (1: Good, 0: Bad)", options=[1, 0])

# Predict button
if st.button("Predict"):
    # Prepare input for prediction
    input_data = np.array([[applicant_income, coapplicant_income, loan_amount, credit_history]])
    prediction = model.predict(input_data)
    result = "Approved" if prediction[0] == 1 else "Rejected" 
    print("Try to maintain good credit score")

    # Display result
    st.subheader(f"Loan Status: {result},try to maintain good credit score")



