from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title='ML prediction API',
    description='Production style API structure',
    version='1.0'
)

app.include_router(router)