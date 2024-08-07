#!/usr/bin/python3
"""3 - python_route module"""
from flask import Flask, request


app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello():
    """display to display hello hbnb

    Returns:
        the string hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display():
    """Method to display hbnb"""
    return "HBNB"


@app.route("/c/<text>")
def display_c(text):
    """Method to display c following by the text message"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Pyton modeule to display python is cool"""
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
