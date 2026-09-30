from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib

app = FastAPI()

model = joblib.load('iris_model.joblib')
stmodel = joblib.load('iris_stscaled_model.joblib')

class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)

@app.get('/')
def home():
    return {
        'message': 'Iris ML API is running'
    }

@app.get('/health')
def get_health():
    return {
        'status': 'healthy'
    }

@app.post('/predict')
def predict(data: IrisInput):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    prediction = model.predict(features)
    probabilities = model.predict_proba(features)
    stprediction = stmodel.predict(features)
    stprobabilities = stmodel.predict_proba(features)

    return {
        'prediction': prediction.item(),
        'probabilities': probabilities.tolist(),
        'stprediction': stprediction.item(),
        'stprobabilities': stprobabilities.tolist()
    }