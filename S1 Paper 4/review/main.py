from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("model.joblib")

class PInput(BaseModel):
    d1: int
    d2: int

@app.get("/")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: PInput):

    features = [[
        data.d1,
        data.d2
    ]]

    prediction = model.predict(features)[0]

    return {"prediction": int(prediction)}