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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
