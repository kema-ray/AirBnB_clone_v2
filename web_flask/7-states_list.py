#!/usr/bin/python3
'''
A simple Flask web application
'''
from flask import Flask, render_template
from models import storage
from models import *


app = Flask(__name__)
'''
Flask application instance
'''
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''
    The states_list page
    '''
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def flask_teardown(exception):
    '''
    closes the storage on teardown
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
