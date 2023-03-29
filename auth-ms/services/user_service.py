import random
import re
import string
import uuid

from app import db
from models import User


def get_user_by_username(username) -> User:
    return User.query.filter(User.username == username.lower()).first()


def get_user_by_id(id) -> User:
    return User.query.filter(User.id == id).first()


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


def update_refresh_token(id, refresh_token) -> bool:
    try:
        user = get_user_by_id(id)
        if user:
            user.refresh_token = refresh_token
            db.session.add(user)
            db.session.commit()
            return True
        return False
    except Exception as e:
        print("<failed to update refresh_token in db>", e)
        return False


from .jwt_service import generate_tokens


def create_user(username, nickname, password: str) -> tuple[dict, int]:
    """Returns jwt-tokens, or mistakes"""
    if not username or not password:
        return {"message": "Username or password is missing"}, 401

    if not _is_valid_username(username):
        return {
            "message": "Usernames with the `guest-` prefix are forbidden"
        }, 409

    try:
        is_user_exists = db.session.query(
            db.exists().where(User.username == username)
        ).scalar()
        if is_user_exists:
            return {"message": "This username is already taken"}, 409

        user = User(username=username, nickname=nickname, password=password)
        db.session.add(user)
        db.session.commit()

        json_answer, status_code = generate_tokens(user=user, is_guest=False)
        return json_answer, status_code

    except Exception as e:
        print("<failed to send a create-query to the database:>", e)
        return {"message": "failed to write the user to the db"}, 500


def create_guest(nickname: str) -> tuple[dict, int]:
    user = User(
        id=uuid.uuid4(),
        username=_generate_guest_username(),
        nickname=nickname,
    )
    json_answer, status_code = generate_tokens(user=user, is_guest=True)
    return json_answer, status_code


def _is_valid_username(username: str):
    """Usernames with the `guest-` prefix are forbidden"""

    if re.match("^guest-.*", username):
        return False
    return True


def _generate_guest_username() -> str:
    random_string = _get_random_string(5)
    return f"guest-{random_string}"


def _get_random_string(size=5) -> str:
    chars = string.ascii_lowercase + string.digits
    random_string = ""
    for i in range(size):
        random_string += random.choice(chars)
    return random_string
