from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Customer Prediction API",
    description="ML inference API",
    version="1.0.0"
)


class PredictionRequest(BaseModel):
    age: int = Field(
        ge=0,
        le=120,
        description="Customer age"
    )

    income: float = Field(
        gt=0,
        description="Annual income"
    )


class PredictionResponse(BaseModel):
    prediction: int
    probability: float


@app.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Generate customer prediction",
    description="Uses the trained ML model to generate a prediction."
)
def predict(data: PredictionRequest):

    # Normally model.predict() would be used here

    return {
        "prediction": 1,
        "probability": 0.94
    }