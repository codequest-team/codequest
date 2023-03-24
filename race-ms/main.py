from fastapi import FastAPI
from api import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Regex Racing',
    description='CodeQuest Regex Recing game microservice',
    version='1.0.0',
)

app.include_router(router)