#!/usr/bin/python3
"""
This is a Flask web application for the HBNB project.
It displays an HTML page with information about States, Cities, Amenities,
and Places using data from the HBNB storage engine.
The web application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb: Displays a dynamic HTML page with information about States,
           Cities, Amenities, and Places.
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display the HBNB HTML page."""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    cities = sorted(storage.all("City").values(), key=lambda x: x.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda x: x.name)
    places = sorted(storage.all("Place").values(), key=lambda x: x.name)
    return render_template('100-hbnb.html', states=states, cities=cities,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
