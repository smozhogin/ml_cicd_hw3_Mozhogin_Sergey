import os
import joblib
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_PATH = os.path.join('models', 'model.pkl')
model = joblib.load(MODEL_PATH)

app = FastAPI()
VERSION = os.getenv('MODEL_VERSION', 'v1.0.0')

class PredictRequest(BaseModel):
    X: List[float]

@app.get('/health')
def health():
    return {
        "Health": "OK",
        "Version": VERSION
    }

@app.post('/predict')
def predict(req: PredictRequest):
    X = [req.X]
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0]

    return {
        'Inference': int(pred),
        'Probabilities': proba.tolist(),
        'Version': VERSION
    }