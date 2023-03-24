from flask import jsonify

from app import app


@app.route("/")
def hello_world():
    return jsonify({"message": "Hello world! It works!"})
