**Credit Score Classifier - README**

---

### Project Title:
**Credit Score Classifier - Flask API & Streamlit Interface**

---

### Project Description:
This project is a full-stack machine learning application designed to classify a person's credit score into three categories: **Good**, **Standard**, or **Bad**. The core classifier was built using the **XGBoost** algorithm, embedded in a **pipeline** that includes **StandardScaler**, and trained on a cleaned dataset. It features both a **Flask API** for backend deployment and a **Streamlit app** for user interaction.

The model is optimized with **RandomizedSearchCV**, and all preprocessing steps, including **label encoding** and feature scaling, were included in a reproducible workflow. The goal was to simulate a real-world, end-to-end machine learning deployment for a multi-class classification task.

---

### Features:
- Multi-class classification: `Good`, `Standard`, `Bad`
- Modular Flask backend
- Streamlit interface for real-time predictions
- JSON schema validation for input
- Serialized model and label encoder for production use

---

### Tech Stack:
- Python 3.12
- XGBoost, Scikit-learn
- Flask
- Streamlit
- Pandas, NumPy
- joblib
- jsonschema

---

### How to Use:

**1. Clone the Repository**
```bash
git clone https://github.com/Nonny-123/Credit-Score-Classifier.git
cd Credit-Score-Classifier
```

**2. Set Up Environment**
```bash
pip install -r requirements.txt
```

**3. Start Flask API**
```bash
cd flask_app
python app.py
```

**4. Start Streamlit App**
```bash
cd streamlit_app
streamlit run app.py
```

---

### Sample JSON Input for API:
```json
{
  "Occupation": 2,
  "Monthly_Inhand_Salary": 45000,
  "Num_Credit_Card": 3,
  "Interest_Rate": 14,
  "Num_of_Loan": 2,
  "Delay_from_due_date": 4,
  "Num_of_Delayed_Payment": 2,
  "Changed_Credit_Limit": 1.5,
  "Num_Credit_Inquiries": 3,
  "Credit_Mix": 1,
  "Credit_Utilization_Ratio": 0.6,
  "Payment_of_Min_Amount": 1,
  "Total_EMI_per_month": 5000,
  "Amount_invested_monthly": 10000,
  "Payment_Behaviour": 1,
  "Monthly_Balance": 15000,
  "Age_Cleaned": 32,
  "Debt_to_Income_Ratio": 0.3,
  "Credit_History_Age_Months": 60
}
```

---

### Project Structure:
- `models/` - Trained model and label encoder
- `flask_app/` - API logic and routes
- `streamlit_app/` - UI components for prediction

---

### Author:
**Okonji Chukwunonyelim Gabriel**
ML Engineer | Data Scientist

- GitHub: [Nonny-123](https://github.com/Nonny-123)
- Medium: [@nonnyokonji](https://medium.com/@nonnyokonji/introduction-03273639585b)


