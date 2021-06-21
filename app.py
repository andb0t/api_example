from flask import Flask, request

import random

import model


app = Flask(__name__)


@app.route("/")
def home():
    """Greet the course."""
    return 'Hello!'


@app.route("/random/")
def random_number():
    """Return a random number."""
    number = random.random()
    return f'Your random number: {number}'


if __name__ == "__main__":
    app.run(debug=True)
