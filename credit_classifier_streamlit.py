import joblib
import pandas as pd
import streamlit as st

model = joblib.load("credit_classification_xgb.pkl")
le = joblib.load("credit_classification_le.pkl")

st.title("Credit Score Classifier")

Occupation = st.selectbox("Occupation", options=['Scientist', 'Null', 'Teacher', 'Engineer', 'Entrepreneur'
                                                  'Developer', 'Lawyer', 'Media_Manager', 'Doctor', 'Journalist',
                                                  'Manager', 'Accountant', 'Musician', 'Mechanic', 'Writer', 'Architect'])
Monthly_Inhand_Salary = st.number_input("Monthly Inhand Salary (303 - 15204)", min_value=303.6454166666666, max_value=15204.633333333331)
Num_Credit_Card = st.number_input("Number of Credit Cards (0 - 1499)", min_value=0, max_value=1499)
Interest_Rate = st.number_input("Interest Rate (1 - 5797)", min_value=1, max_value=5797)
Num_of_Loan = st.number_input("Number of Loans (1 - 9)", min_value=1, max_value=9)
Delay_from_due_date = st.number_input("Delay from due date(0 - 67)", min_value=0, max_value=67)
Num_of_Delayed_Payment = st.number_input("Num of Delayed Payment (0 - 4397)", min_value=0, max_value=4397)
Changed_Credit_Limit = st.number_input("Changed Credit Limit (0 - 36.97)", min_value=-6.49, max_value=36.97)
Num_Credit_Inquiries = st.number_input("Number of Credit Inquiries (0 - 2597)", min_value=0, max_value=2597)
Credit_Mix = st.selectbox("Credit Mix", options=['Standard', 'Good', 'Bad'])
Credit_Utilization_Ratio = st.number_input("Credit Utilization Ratio (20 - 50)", min_value=20.0, max_value=50.00000000000001)
Payment_of_Min_Amount = st.selectbox("Payment of Min Amount", options=["NO", "Yes"])
Total_EMI_per_month = st.number_input("Total EMI per month (0 - 82331)", min_value=0.0, max_value=82331.0)
Amount_invested_monthly = st.number_input("Amount invested monthly (0 - 1977)", min_value=0.0, max_value=1977.326102249349)
Payment_Behaviour = st.selectbox("Payment Behaviour", options=['High_spent_Small_value_payments', 'Low_spent_Large_value_payments', 'Low_spent_Medium_value_payments'
                                                                'Low_spent_Small_value_payments', 'High_spent_Medium_value_payments', 'High_spent_Large_value_payments'])
Monthly_Balance = st.number_input("Monthly Balance (0 - 1602)", min_value=0.0077596647753352, max_value=1602.0405189622518)
Age_Cleaned = st.number_input("Age (14 - 118)", min_value=14, max_value=118)
Debt_to_Income_Ratio = st.number_input("Debt to Income Ratio (4.00 - 0.1 )", min_value=4.086799670023885e-07, max_value=0.6832515548332656)
Credit_History_Age_Months = st.number_input("Credit History Age Months (1 - 404)", min_value=1, max_value=404)

input_data = {
    "Occupation": Occupation,
    "Monthly_Inhand_Salary": Monthly_Inhand_Salary,
    "Num_Credit_Card": Num_Credit_Card,
    "Interest_Rate": Interest_Rate,
    "Num_of_Loan": Num_of_Loan,
    "Delay_from_due_date": Delay_from_due_date,
    "Num_of_Delayed_Payment": Num_of_Delayed_Payment,
    "Changed_Credit_Limit": Changed_Credit_Limit,
    "Num_Credit_Inquiries": Num_Credit_Inquiries,
    "Credit_Mix": Credit_Mix,
    "Credit_Utilization_Ratio": Credit_Utilization_Ratio,
    "Payment_of_Min_Amount": Payment_of_Min_Amount,
    "Total_EMI_per_month": Total_EMI_per_month,
    "Amount_invested_monthly": Amount_invested_monthly,
    "Payment_Behaviour": Payment_Behaviour,
    "Monthly_Balance": Monthly_Balance,
    "Age_Cleaned": Age_Cleaned,
    "Debt_to_Income_Ratio": Debt_to_Income_Ratio,
    "Credit_History_Age_Months": Credit_History_Age_Months
}

def predict_credit(input_data):
    input_df = pd.DataFrame([input_data])

    for col in ['Credit_Mix', 'Payment_of_Min_Amount', 'Payment_Behaviour', 'Credit_Score', 'Occupation']:
        if col in input_df.columns:
            input_df[col] = le.fit_transform(input_df[col]) 

    prediction = model.predict(input_df)
    return prediction

if st.button("Predict Credit Score Classification"):
    prediction = predict_credit(input_data)

    if prediction == 0:
        st.info("Credit Classification: GOOD")
    elif prediction == 1:
        st.info("Credit Classification: BAD")
    elif prediction == 2:
        st.info("Credit Classification: STANDARD")
    

