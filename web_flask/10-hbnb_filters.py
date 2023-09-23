#!/usr/bin/python3
"""
Flask web application to display an HTML page with Airbnb filters
The web application listening on 0.0.0.0, port 5000
Load all cities of a State:
    If The storage engine is DBStorage, it uses cities relationship
    Otherwise, it uses the public getter method cities
After each request you must remove the current SQLAlchemy Session
Routes:
    /hbnb_filters: display a HTML page
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """Display the HTML page with Airbnb filters."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)

    return render_template('10-hbnb_filters.html',
                           states=states, cities=cities, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
