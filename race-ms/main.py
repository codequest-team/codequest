from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import router
from config import settings

app = FastAPI(
    title='Regex Racing',
    description='CodeQuest Regex Recing game microservice',
    version='1.0.0',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS.split(','),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)