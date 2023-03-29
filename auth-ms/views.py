from flask import jsonify, request

from app import app
from services.user_service import (
    create_guest,
    create_user,
    get_user_by_username,
    remove_refresh_token,
)
from services.jwt_service import (
    generate_tokens,
    refresh_tokens,
    token_required,
)


@app.route("/get-guest", methods=["POST"])
def get_guest():
    """Makes user with random data and returns tokens"""

    json_answer, status_code = create_guest(request.form.get("nickname"))
    return jsonify(json_answer), status_code


@app.route("/login", methods=["POST"])
def login():
    """Authenticates and returns tokens"""

    username = request.form.get("username")
    password = request.form.get("password")

    user = get_user_by_username(username)

    if user and user.verify_password(password):
        json_answer, status_code = generate_tokens(user=user, is_guest=False)
        return jsonify(json_answer), status_code
    else:
        return jsonify({"message": "Invalid username or password"}), 401


@app.route("/signup", methods=["POST"])
def signup():
    """Creates a user and returns tokens"""

    json_answer, status_code = create_user(
        username=request.form.get("username"),
        nickname=request.form.get("nickname"),
        password=request.form.get("password"),
    )
    return jsonify(json_answer), status_code


@app.route("/refresh")
def refresh():
    """Returns new tokens or mistakes"""

    refresh_token = request.headers.get("Authorization")
    json_answer, status_code = refresh_tokens(refresh_token)
    return jsonify(json_answer), status_code


@app.route("/verify")
@token_required
def verify(user):
    """Verifies if the token is valid"""

    return jsonify({"message": "Access token is valid"}), 200


@app.route("/get-credentials")
@token_required
def get_credentials(user):
    """Decodes token and return user's credentials"""

    return jsonify({"username": user.username, "nickname": user.nickname}), 200


@app.route("/logout")
@token_required
def logout(user):
    """Deletes refresh_token from database"""

    json_answer, status_code = remove_refresh_token(user.id)
    return jsonify(json_answer), status_code
