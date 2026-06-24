import pandas as pd
from api.services.model_loader import load_risk_model, load_claim_model

def predict_risk_result(data: dict):
    model = load_risk_model()
    # Convert input data to DataFrame
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]
    response = {
        "prediction": prediction
    }
    
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_df)[0]
        response["probabilities"] = probabilities.tolist()
    return response

def predict_claim_result(data: dict):
    model = load_claim_model()
    # Convert input data to DataFrame
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]
    response = {
        "prediction": prediction
    }
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_df)[0]
        response["probabilities"] = probabilities.tolist()
    return response