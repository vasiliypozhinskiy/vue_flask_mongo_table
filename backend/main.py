from app import socketio
from app.view import *

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
