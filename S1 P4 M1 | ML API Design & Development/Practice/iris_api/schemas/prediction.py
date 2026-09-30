from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):

    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)

class PredictionResponse(BaseModel):

    prediction: int
    probability: float
    species: str