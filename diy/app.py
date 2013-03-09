from flask import Flask
import platform
app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello from Flask'

@app.route("/info")
def info():
    return platform.python_version()
