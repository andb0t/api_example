from flask import Flask, request

import random

import model


app = Flask(__name__)


@app.route("/")
def home():
    """Greet the course."""
    return 'Hello Back Belt Course!'


if __name__ == "__main__":
    app.run(debug=True)
