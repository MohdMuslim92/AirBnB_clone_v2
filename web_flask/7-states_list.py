#!/usr/bin/python3
"""
    This module contains a simple Flask web application that displays a list of
    states.

    The script starts a Flask web application:
        - Listening on 0.0.0.0, port 5000
        - Defines a single route: /states_list

    Routes:
        - /states_list: Display a HTML page containing a list of all State
        objects present in DBStorage, sorted by name (A->Z).
        Each state is listed with its ID and name.
"""

from flask import Flask, render_template
from models import *
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
        Display a list of states sorted by name.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_storage(exception):
    """
        Remove the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
