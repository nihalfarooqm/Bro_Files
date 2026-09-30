from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# class UserInput(BaseModel):
#     age: int = Field(gt=0, lt=120)
#     income: float = Field(gt=0)

# @app.post('/predict')
# def predict(data: UserInput):
#     return {
#         'age': data.age,
#         'income': data.income
#     }

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict")
def predict(data: IrisInput):

    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    # prediction = model.predict(features)

    prediction = 0

    return {
        "prediction": prediction
    }