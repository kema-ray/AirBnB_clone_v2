#!/usr/bin/python3
"""
Flask Web application
"""
from flask import Flask


app = Flask(__name__)
"""
Flask application instance
"""
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    Home Page
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Hbnb Page
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    """
    The c Page
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    """
    The python Page
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_page(n):
    """
    The number Page
    """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
