from datetime import datetime
from functools import wraps
from typing import Literal, TypedDict

import jwt  # type: ignore
from flask import jsonify, request

from app import app
from models import User

from .user_service import get_user_by_id, update_refresh_token


class JwtPayload(TypedDict):
    id: str
    username: str
    nickname: str
    is_guest: bool
    exp: datetime
    token_type: Literal["access", "refresh"]


def _generate_a_token(user, is_guest, exp_delta, token_type) -> str:
    payload: JwtPayload = {
        "id": str(user.id),
        "username": user.username,
        "nickname": user.nickname,
        "is_guest": is_guest,
        "exp": datetime.utcnow() + exp_delta,
        "token_type": token_type,
    }
    return jwt.encode(
        payload,
        app.config["SECRET_KEY"],
        algorithm="HS256",
    )


def generate_tokens(user: User, is_guest: bool) -> tuple[dict, int]:
    access_token = _generate_a_token(
        user=user,
        is_guest=is_guest,
        exp_delta=app.config["JWT_ACCESS_EXPIRATION_DELTA"],
        token_type="access",
    )
    refresh_token = _generate_a_token(
        user=user,
        is_guest=is_guest,
        exp_delta=app.config["JWT_REFRESH_EXPIRATION_DELTA"],
        token_type="refresh",
    )
    tokens = {"access_token": access_token, "refresh_token": refresh_token}

    if is_guest:
        return tokens, 200
    else:
        is_result_success = update_refresh_token(user.id, refresh_token)
        if not is_result_success:
            return {"message": "Can't update refresh_token in db"}, 500

        return tokens, 200


def refresh_tokens(refresh_token) -> tuple[dict, int]:
    if not refresh_token:
        return {"message": "Refresh token is missing!"}, 401

    try:
        payload = jwt.decode(
            refresh_token, app.config["SECRET_KEY"], algorithms=["HS256"]
        )
    except jwt.ExpiredSignatureError:
        return {"message": "Refresh token has expired!"}, 401
    except jwt.InvalidTokenError:
        return {"message": "Refresh token is invalid!"}, 401

    if payload.get("token_type") != "refresh":
        return {"message": "Refresh token is invalid!"}, 401
    is_guest = payload.get("is_guest")
    if is_guest:
        user = User(
            id=payload.get("id"),
            username=payload.get("username"),
            nickname=payload.get("nickname"),
        )
    else:
        user = get_user_by_id(payload.get("id"))
        if user.refresh_token != refresh_token:
            return {"message": "Refresh token is invalid!"}, 401

    json_answer, status_code = generate_tokens(user, is_guest)
    return json_answer, status_code


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
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Access token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Access token is invalid!"}), 401

        if payload.get("token_type") != "access":
            return jsonify({"message": "Access token is invalid!"}), 401

        user = User(
            id=payload.get("id"),
            username=payload.get("username"),
            nickname=payload.get("nickname"),
        )

        return func(user, *args, **kwargs)

    return wrapper
