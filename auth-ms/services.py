from datetime import datetime
from functools import wraps
from typing import Literal, TypedDict

import jwt  # type: ignore
from flask import jsonify, request

from app import app, db
from models import User


class JwtAccessPayload(TypedDict):
    id: str
    username: str
    exp: datetime
    token_type: Literal["access"]


class JwtRefreshPayload(TypedDict):
    id: str
    exp: datetime
    token_type: Literal["refresh"]


def get_user_by_username(username) -> User:
    return User.query.filter(User.username == username.lower()).first()


def get_user_by_id(id) -> User:
    return User.query.filter(User.id == id).first()


def update_refresh_token(id, refresh_token) -> bool:
    try:
        user = get_user_by_id(id)
        user.refresh_token = refresh_token
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        print("<failed to update refresh_token in db>", e)
        return False


def remove_refresh_token(id) -> tuple[dict, int]:
    try:
        user = get_user_by_id(id)
        if user:
            user.refresh_token = None
            db.session.add(user)
            db.session.commit()
        return {"message": "Refresh token was deleted"}, 200
    except Exception as e:
        print("<failed to update update entry in db>", e)
        return {"message": "failed to update update entry in db"}, 500


def create_user(user: User) -> tuple[dict, int]:
    """Returns jwt-tokens, or mistakes"""
    try:
        is_user_exists = db.session.query(
            db.exists().where(User.username == user.username)
        ).scalar()
        if is_user_exists:
            return {"message": "This username is already taken"}, 409

        db.session.add(user)
        db.session.commit()

        json_answer, status_code = generate_tokens(user)
        return json_answer, status_code

    except Exception as e:
        print("<failed to send a create-query to the database:>", e)
        return {"message": "failed to write the user to the db"}, 500


def _generate_access_token(user: User) -> str:
    payload: JwtAccessPayload = {
        "id": str(user.id),
        "username": user.username,
        "exp": datetime.utcnow() + app.config["JWT_ACCESS_EXPIRATION_DELTA"],
        "token_type": "access",
    }
    return jwt.encode(
        payload,
        app.config["SECRET_KEY"],
        algorithm="HS256",
    )


def _generate_refresh_token(user: User) -> str:
    payload: JwtRefreshPayload = {
        "id": str(user.id),
        "exp": datetime.utcnow() + app.config["JWT_REFRESH_EXPIRATION_DELTA"],
        "token_type": "refresh",
    }
    return jwt.encode(
        payload,
        app.config["SECRET_KEY"],
        algorithm="HS256",
    )


def generate_tokens(user: User) -> tuple[dict, int]:
    access_token = _generate_access_token(user)
    refresh_token = _generate_refresh_token(user)

    is_result_success = update_refresh_token(user.id, refresh_token)

    if is_result_success:
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }, 200
    return {"message": "Can't update refresh_token in db"}, 500


def refresh_tokens(refresh_token) -> tuple[dict, int]:
    if not refresh_token:
        return {"message": "Refresh token is missing!"}, 401

    try:
        payload = jwt.decode(
            refresh_token, app.config["SECRET_KEY"], algorithms=["HS256"]
        )
        user = get_user_by_id(payload.get("id"))
        if (
            payload.get("token_type") != "refresh"
            or user.refresh_token != refresh_token
        ):
            return {"message": "Refresh token is invalid!"}, 401
    except jwt.ExpiredSignatureError:
        return {"message": "Refresh token has expired!"}, 401
    except jwt.InvalidTokenError:
        return {"message": "Refresh token is invalid!"}, 401

    json_answer, status_code = generate_tokens(user)
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
            if payload.get("token_type") != "access":
                return jsonify({"message": "Access token is invalid!"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Access token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Access token is invalid!"}), 401

        return func(payload.get("id"), *args, **kwargs)

    return wrapper
