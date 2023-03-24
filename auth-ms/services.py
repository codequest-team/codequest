from datetime import datetime
from functools import wraps
from typing import Literal, TypedDict

import jwt  # type: ignore
from flask import jsonify, request

from app import app


class JwtPayload(TypedDict):
    username: str
    exp: datetime
    token_type: Literal["access", "refresh"]


# Example user database. { username: {password: "val", refresh_token: "val"} }
users = {
    "user1": {"password": "abc"},
    "user2": {"password": "abc"},
}


def get_user(username):
    # Find user in database
    return users.get(username)


def _generate_access_token(username) -> str:
    payload: JwtPayload = {
        "username": username,
        "exp": datetime.utcnow() + app.config["JWT_ACCESS_EXPIRATION_DELTA"],
        "token_type": "access",
    }
    return jwt.encode(
        payload,
        app.config["SECRET_KEY"],
        algorithm="HS256",
    )


def _generate_refresh_token(username) -> str:
    payload: JwtPayload = {
        "username": username,
        "exp": datetime.utcnow() + app.config["JWT_REFRESH_EXPIRATION_DELTA"],
        "token_type": "refresh",
    }
    return jwt.encode(
        payload,
        app.config["SECRET_KEY"],
        algorithm="HS256",
    )


def generate_tokens(username) -> tuple[str, str]:
    access_token = _generate_access_token(username)
    refresh_token = _generate_refresh_token(username)

    # Save refresh in db for single use
    users[username]["refresh_token"] = refresh_token

    return access_token, refresh_token


def refresh_tokens(refresh_token) -> tuple[dict, int]:
    if not refresh_token:
        return {"message": "Refresh token is missing!"}, 401

    try:
        payload = jwt.decode(
            refresh_token, app.config["SECRET_KEY"], algorithms=["HS256"]
        )
        if (
            payload.get("token_type") != "refresh"
            or users[payload.get("username")].get("refresh_token")
            != refresh_token
        ):
            return {"message": "Refresh token is invalid!"}, 401
    except jwt.ExpiredSignatureError:
        return {"message": "Refresh token has expired!"}, 401
    except jwt.InvalidTokenError:
        return {"message": "Refresh token is invalid!"}, 401

    access_token, refresh_token = generate_tokens(payload.get("username"))
    return {"access_token": access_token, "refresh_token": refresh_token}, 200


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        access_token = request.headers.get("Authorization")
        if not access_token:
            return jsonify({"message": "Access token is missing!"}), 401

        try:
            payload = jwt.decode(
                access_token, app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            if payload.get("token_type") != "access":
                return jsonify({"message": "Access token is invalid!"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Access token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Access token is invalid!"}), 401

        return func(payload.get("username"), *args, **kwargs)

    return wrapper
