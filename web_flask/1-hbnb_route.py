#!/usr/bin/python3
"""inh instance"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """first route function"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_world_hbnb():
    """s route function"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
