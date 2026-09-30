from fastapi import APIRouter
from schemas.prediction import PredictionRequest, PredictionResponse
from services.prediction_service import make_prediction

router = APIRouter()

@router.post(
    '/predict',
    response_model=PredictionResponse
)
def predict(data: PredictionRequest):

    prediction, probability, species = make_prediction(
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    )

    return {
        'prediction': prediction,
        'probability': probability,
        'species': species
    }