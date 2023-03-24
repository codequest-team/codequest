from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from api import router
from config import settings

app = FastAPI(
    title='Regex Racing',
    docs_url="/",
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

register_tortoise(
    app,
    db_url=settings.get_db_uri(),
    modules={"models": ["database.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
    )


app.include_router(router)