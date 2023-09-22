#!/usr/bin/python3
"""
This is a simple Flask web application.
The script starts a Flask web application:
    Listening on 0.0.0.0, port 5000
    Routes:
        /: display 'Hello HBNB!'
        /hbnb: display 'HBNB'
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    """
    Route that displays "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that displays "HBNB".
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
