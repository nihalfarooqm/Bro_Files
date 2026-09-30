from fastapi import APIRouter
from schemas.prediction import PredictionRequest, PredictionResponse
from services.prediction_services import make_prediction

router = APIRouter()

@router.post('/predict', response_model=PredictionResponse)
def predict(data: PredictionRequest):

    prediction, probability = make_prediction(
        data.age,
        data.income
    )

    return {
        'prediction': int(prediction),
        'probability': float(probability)
    }