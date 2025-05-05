from flask import Blueprint, request, jsonify
from jsonschema import validate, ValidationError
import logging
from .utils import make_prediction

logging.basicConfig(level=logging.ERROR)

routes = Blueprint('routes', __name__)

# Define the expected JSON schema for the input data
credit_score_input_schema = {
    "type": "object",
    "properties": {
        "Occupation": {"type": "integer"},
        "Monthly_Inhand_Salary": {"type": "number"},
        "Num_Credit_Card": {"type": "integer"},
        "Interest_Rate": {"type": "integer"},
        "Num_of_Loan": {"type": "integer"},
        "Delay_from_due_date": {"type": "integer"},
        "Num_of_Delayed_Payment": {"type": "number"},
        "Changed_Credit_Limit": {"type": "number"},
        "Num_Credit_Inquiries": {"type": "integer"},
        "Credit_Mix": {"type": "integer"},
        "Credit_Utilization_Ratio": {"type": "number"},
        "Payment_of_Min_Amount": {"type": "integer"},
        "Total_EMI_per_month": {"type": "number"},
        "Amount_invested_monthly": {"type": "number"},
        "Payment_Behaviour": {"type": "integer"},
        "Monthly_Balance": {"type": "number"},
        "Age_Cleaned": {"type": "integer"},
        "Debt_to_Income_Ratio": {"type": "number"},
        "Credit_History_Age_Months": {"type": "number"}
    },
    "required": [
        "Occupation", "Monthly_Inhand_Salary", "Num_Credit_Card", "Interest_Rate",
        "Num_of_Loan", "Delay_from_due_date", "Num_of_Delayed_Payment",
        "Changed_Credit_Limit", "Num_Credit_Inquiries", "Credit_Mix",
        "Credit_Utilization_Ratio", "Payment_of_Min_Amount", "Total_EMI_per_month",
        "Amount_invested_monthly", "Payment_Behaviour", "Monthly_Balance",
        "Age_Cleaned", "Debt_to_Income_Ratio", "Credit_History_Age_Months"
    ],
    "additionalProperties": False
}

@routes.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        try:
            validate(instance=data, schema=credit_score_input_schema)
        except ValidationError as ve:
            logging.error(f"Input data validation error: {ve}")
            return jsonify({"error": f"Invalid input data: {ve.message}"}), 400

        prediction = make_prediction(data)
        return jsonify({"credit_score_class": prediction})
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500