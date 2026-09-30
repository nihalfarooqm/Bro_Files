from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    age: int = Field(ge=18, le=120)
    income: float = Field(gt=0)

class PredictionResponse(BaseModel):
    prediction: int
    probability: float