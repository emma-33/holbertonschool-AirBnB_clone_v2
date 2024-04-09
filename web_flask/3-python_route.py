#!/usr/bin/python3
"""Starts a Flask web application"""
from markupsafe import escape
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Prints Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Prints HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_c(text):
    """Prints "C" followed by the value of the text variable"""
    return f"C {escape(text).replace('_', ' ')}"


@app.route("/python/", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def hello_python(text):
    """Prints "Python" followed by the value of the text variable"""
    return f"Python {escape(text).replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
