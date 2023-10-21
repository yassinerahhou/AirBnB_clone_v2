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
    """route with variable"""
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """python route"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
