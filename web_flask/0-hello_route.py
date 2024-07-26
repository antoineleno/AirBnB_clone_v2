#!/usr/bin/python3
"""0-hello_router module"""
from flask import Flask


app = Flask("__name__")


@app.route("/", strict_slashes=False)
def display():
    """display to display hello hbnb

    Returns:
        the string hello HBNB!
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
