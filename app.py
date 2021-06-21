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


@app.route("/random/plus")
def random_number_plus():
    """Return a random number + the input."""
    argument = request.args.get('input')
    try:
        number = random.random() + float(argument)
        return f'Your random number plus {argument}: {number}'
    except ValueError:
        return f'Your argument has to be a number! ({argument} is an invalid argument)', 400


if __name__ == "__main__":
    app.run(debug=True)
