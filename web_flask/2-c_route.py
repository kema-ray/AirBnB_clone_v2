#!/usr/bin/python3
<<<<<<< HEAD
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 3d2627b123b2b6c59c48a1fc32be2cb4b652435f
