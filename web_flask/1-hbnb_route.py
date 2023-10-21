#!/usr/bin/python3
from flask import Flask
"""inh instance"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
"""first route function"""


def hello_world():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
"""s route function"""


def hello_world_hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
