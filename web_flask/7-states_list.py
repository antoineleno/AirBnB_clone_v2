#!/usr/bin/python3
"""Flask application with various routes"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Display all the states from storage"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown(exception):
    """Reload each time the content of storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
