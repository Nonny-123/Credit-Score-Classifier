import joblib
import pandas as pd

model = joblib.load("credit_classification_xgb.pkl")
label_encoder = joblib.load("credit_classification_le.pkl")

def make_prediction(input_data):
    df = pd.DataFrame([input_data])
    pred_encoded = model.predict(df)[0]
    pred_label = label_encoder.inverse_transform([int(pred_encoded)])[0]
    return pred_label