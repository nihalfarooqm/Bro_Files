from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title='Iris API Practice',
    description='Iris Classification model API Practice',
    version='1.0'
)

app.include_router(router)

@app.get('/health')
def health():
    return {
        'status': 'healthy'
    }