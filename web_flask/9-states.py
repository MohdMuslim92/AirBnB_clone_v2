#!/usr/bin/python3
"""Flask web application to list and display states and cities.
The script that starts a Flask web application  listening on 0.0.0.0, port 5000
Load all cities of a State:
    If the storage engine is DBStorage, it uses cities relationship
    Otherwise, it uses the public getter method cities
After each request it removes the current SQLAlchemy Session:
Routes:
    - /states: display a HTML page: (inside the tag BODY)
    - H1 tag: “States”
    - UL tag: with the list of all State objects present in DBStorage sorted
      by name (A->Z) tip
    - LI tag: description of one State: <state.id>: <B><state.name></B>
    - /states/<id>: display a HTML page: (inside the tag BODY)
        If a State object is found with this id:
            H1 tag: “State: ”
            H3 tag: “Cities:”
            UL tag: with the list of City objects linked to the State sorted
              by name (A->Z)
            LI tag: description of one City: <city.id>: <B><city.name></B>
        Otherwise:
            H1 tag: “Not found!”
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Close the SQLAlchemy session."""
    storage.close()


@app.route('/states', strict_slashes=False)
def list_states():
    """Display a list of states."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def display_state(state_id):
    """Display information about a specific state."""
    state = storage.get(State, state_id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
