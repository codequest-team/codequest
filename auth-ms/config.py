from datetime import timedelta
from os import getenv
from os.path import dirname, join

from dotenv import load_dotenv  # type: ignore

load_dotenv(join(dirname(__file__), "../.envs/.local/.auth-ms"))
load_dotenv(join(dirname(__file__), "../.envs/.local/.postgres"))


class Configuration:
    DEBUG = True
    JWT_ACCESS_EXPIRATION_DELTA = timedelta(minutes=30)
    JWT_REFRESH_EXPIRATION_DELTA = timedelta(days=30)
    SECRET_KEY = getenv("JWT_SECRET_KEY")

    CORS_ORIGINS = getenv("AUTH_CORS_ORIGINS").split(",")

    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
