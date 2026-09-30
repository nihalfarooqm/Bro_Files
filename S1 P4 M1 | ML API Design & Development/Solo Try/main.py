from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field

app = FastAPI(
    title='Try ApI',
    description='A try with different things on different matters',
    version='1.0.0'
)

API_KEY = 'mykey'

class square_Input(BaseModel):
    val : int

class divideInput(BaseModel):
    num : int
    deno: int = Field(gt=0, description='Denominater 0 is undifined')

class ResponseDefine(BaseModel):
    output : float
    output_rounded : int

@app.post(
    '/square',
    summary='Get square',
    description='Find the square of a number'
    )
def square(val_in: square_Input):
    try :
        sq = val_in.val * val_in.val
        return {
            'square': sq
        }
    except Exception:
        raise HTTPException(
            status_code=500,
            detail='Something went wrong, try again later'
        )

@app.post(
    '/cube/{val_in}',
    summary='Get cube',
    description='Find the cube of a number')
def cube(val_in: int):
    return {
        'cube': val_in * val_in * val_in
    }

@app.get('/subjects')
def subjects(subject: str):
    return {
        'subject': subject
    }

@app.post('/divide', response_model=ResponseDefine)
def divide(val: divideInput):
    return {
        'output': val.num / val.deno,
        'output_rounded': int(val.num / val.deno)
    }

@app.get('/users/{user_id}')
def get_user(user_id: int):
    if user_id < 1:
        raise HTTPException(
            status_code=400,
            detail='ueer id should be greater than 0'
        )

    return {
        'user_id': user_id
    }

@app.get('/apikey')
def apikey(x_api_key: str = Header(None)):

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail='invalid key'
        )
    return {
        'pred': 1
    }