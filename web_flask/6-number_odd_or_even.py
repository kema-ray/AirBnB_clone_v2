#!/usr/bin/python3
"""
Flask Web application
"""
from flask import Flask, render_template


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays a HTML page only if n is an integer
    """
    if n % 2 == 0:
        numbered = 'even'
    else:
        numbered = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           numbered=numbered)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
