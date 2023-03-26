from flask import jsonify, request

from app import app
from models import User
from services import (
    create_user,
    generate_tokens,
    get_user_by_id,
    get_user_by_username,
    remove_refresh_token,
    refresh_tokens,
    token_required,
)


@app.route("/login", methods=["POST"])
def login():
    # Find user in database
    username = request.form.get("username")
    password = request.form.get("password")
    user = get_user_by_username(username)

    if user and user.verify_password(password):
        json_answer, status_code = generate_tokens(user)
        return jsonify(json_answer), status_code
    else:
        return jsonify({"message": "Invalid username or password"}), 401


@app.route("/signup", methods=["POST"])
def signup():
    user = User(
        username=request.form.get("username"),
        nickname=request.form.get("nickname"),
        password=request.form.get("password"),
    )

    json_answer, status_code = create_user(user)
    return jsonify(json_answer), status_code


@app.route("/refresh")
def refresh():
    refresh_token = request.headers.get("Authorization")
    json_answer, status_code = refresh_tokens(refresh_token)
    return jsonify(json_answer), status_code


@app.route("/verify")
@token_required
def verify(user_id):
    """Verifies if the token is valid"""

    return jsonify({"message": "Access token is valid"}), 200


@app.route("/get-credentials")
@token_required
def get_credentials(user_id):
    """decode token and return content"""

    user = get_user_by_id(user_id)

    return jsonify({"username": user.username, "nickname": user.nickname}), 200


@app.route("/logout")
@token_required
def logout(user_id):
    """decode token and return content"""

    json_answer, status_code = remove_refresh_token(user_id)
    return jsonify(json_answer), status_code
