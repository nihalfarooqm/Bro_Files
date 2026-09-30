from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib


app = FastAPI(title="ML Prediction API")

model = joblib.load("model.joblib")


class PredictionInput(BaseModel):
    age: int = Field(gt=0, lt=120)
    income: float = Field(gt=0)


class PredictionResponse(BaseModel):
    prediction: int
    confidence: float


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(data: PredictionInput):

    try:
        features = [[
            data.age,
            data.income
        ]]

        prediction = model.predict(features)[0]

        probability = model.predict_proba(features).max()

        return {
            "prediction": int(prediction),
            "confidence": float(probability)
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed"
        )