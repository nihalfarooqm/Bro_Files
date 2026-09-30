from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib

app = FastAPI(
    title='Iris Test',
    description="ML API for Iris flower classification",
    version='1.0.0'
)

model = joblib.load('test_model.joblib')

class PredictionRequest(BaseModel):

    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)

class PredictionResponse(BaseModel):

    prediction: int
    probability: float
    species: str

@app.get('/health')
def health():
    return {
        'status': 'healthy'
    }

@app.post(
    '/predict',
    response_model=PredictionResponse
)
def predict(data: PredictionRequest):

    try:
        X = [[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]]

        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0].max()

        species = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica'
        }

        return {
            'prediction': int(prediction),
            'probability': float(probability),
            'species': species[prediction]
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail='Prediction Failed'
        )