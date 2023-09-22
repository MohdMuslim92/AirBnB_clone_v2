#!/usr/bin/python3
"""
This is a simple Flask web application.
The script starts a Flask web application:
    Listening on 0.0.0.0, port 5000
    Routes:
        /: display 'Hello HBNB!'
        /hbnb: display 'HBNB'
        /c/<text>: display 'C ' followed by the value of the text variable
          (replace underscore _ symbols with a space )
        /python/<text>: display 'Python ', followed by the value of the text
          variable (replace underscore _ symbols with a space )
          The default value of text is 'is coo'
        /number/<n>: display 'n is a number' only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
          H1 tag: “Number: n” inside the tag BODY

"""


from flask import Flask, escape, render_template

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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route that displays "C " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return "C " + escape(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_route(text="is cool"):
    """
    Route that displays "Python ", followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    If no text is provided, use the default value "is cool".
    """
    return "Python " + escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route that displays "n is a number" only if n is an integer.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route that displays an HTML page only if n is an integer:
    H1 tag: "Number: n" inside the BODY tag.
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
