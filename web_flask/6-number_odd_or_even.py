#!/usr/bin/python3
# make instance
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """return HBNB!"""
    return 'HBNB!'


@app.route('/hbnb', strict_slashes=False)
def dispaly_hbnb():
    """display hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_varable():
    """varable function"""
    text = text.replace('_', ' ')
    return 'C ' + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>')
def n_number(n):
    """display n_number"""
    return f'{n}'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_templatee_n(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """check if odd or even"""
    checking = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', checking=checking, n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
