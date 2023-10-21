#!/usr/bin/python3
"""C is fun"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """first route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_world_hbnb():
    """s route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_hbnb(text):
    """route with varable"""
    text = text.replace('_', ' ')
    return "C" + text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
