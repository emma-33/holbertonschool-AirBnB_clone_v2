#!/usr/bin/python3
"""Starts a Flask web application"""
from markupsafe import escape
from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def hello_number(n):
    """Prints "n is a number" only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello_number_template(n):
    """Prints "n is a number" only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def hello_number_odd_or_even(n):
    """Display 6-number_odd_or_even.html template only if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
