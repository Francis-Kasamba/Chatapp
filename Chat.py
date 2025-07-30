#imports

import os
import random
import logging
from datetime import datetime
from typing import Dict

from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"


if __name__ == "__main__":
    app.run(debug=True)
