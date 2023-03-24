from flask import Flask
from flask_cors import CORS  # type: ignore

from config import Configuration

app = Flask(__name__)

app.config.from_object(Configuration)
CORS(app, resources={r"/*": {"origins": app.config["CORS_ORIGINS"]}})
