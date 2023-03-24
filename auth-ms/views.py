from flask import jsonify, request

from app import app
from services import generate_tokens, get_user, refresh_tokens, token_required


@app.route("/login", methods=["POST"])
def login():
    # Find user in database
    username = request.form.get("username")
    password = request.form.get("password")
    user = get_user(username)

    if user and user.get("password") == password:
        access_token, refresh_token = generate_tokens(username)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}
        return jsonify(tokens), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401


@app.route("/refresh")
def refresh():
    refresh_token = request.headers.get("Authorization")
    json_answer, status_code = refresh_tokens(refresh_token)
    return jsonify(json_answer), status_code


@app.route("/verify")
@token_required
def verify(username):
    """Verifies if the token is valid"""

    return jsonify({"message": "Access token is valid"}), 200


@app.route("/get_credentials")
@token_required
def get_credentials(username):
    """decode token and return content"""

    return jsonify({"username": username}), 200
