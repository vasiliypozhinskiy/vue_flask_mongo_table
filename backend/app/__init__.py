from flask import Flask
from flask_socketio import SocketIO

from flask_mongoengine import MongoEngine
from flask_cors import CORS

from app.config import Config

app = Flask(__name__, instance_relative_config=True)

app.config.from_object(Config)

cors = CORS(app, origins='10.1.0.7')
db = MongoEngine(app)

socketio = SocketIO(app, cors_allowed_origins='10.1.0.7', path="/socket")
