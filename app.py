from flask import Flask, request

import json
import random

import model


app = Flask(__name__)


@app.route("/")  # example: http://127.0.0.1:5000/
def home():
    """Greet the course."""
    return 'Hello!'


@app.route("/random/")  # example: http://127.0.0.1:5000/random
def random_number():
    """Return a random number."""
    number = random.random()
    return f'Your random number: {number}'


@app.route("/random/plus")  # example: http://127.0.0.1:5000/random/plus?input=2
def random_number_plus():
    """Return a random number + the input."""
    argument = request.args.get('input')
    try:
        number = random.random() + float(argument)
        return f'Your random number plus {argument}: {number}'
    except ValueError:
        return f'Your argument has to be a number! ({argument} is an invalid argument)', 400


@app.route("/model")  # example: http://127.0.0.1:5000/model?input=2
def call_simple_model():
    """Return the output of the model given the input."""
    argument = request.args.get('input')
    if not argument:
        return f'Input error: argument is required.', 400
    try:
        output = model.my_simple_model(argument)
    except Exception as exc:
        # Warning: never print error details in production
        return f'Internal server error: {exc}', 500
    return f'The output given the argument "{argument}": {output}'


@app.route("/diabetes")  # example: http://127.0.0.1:5000/diabetes?input=[-0.00188201652779104, -0.044641636506989, -0.0514740612388061, -0.0263278347173518, -0.00844872411121698, -0.019163339748222, 0.0744115640787594, -0.0394933828740919, -0.0683297436244215, -0.09220404962683]
def call_real_model():
    """Return the output of the model given the input."""
    argument = request.args.get('input')
    try:
        output = model.my_real_model(argument)
    except TypeError as exc:
        # Warning: never print error details in production
        return f'Internal server error: {exc}', 500
    return f'You successfully called the trained model!<br/><br/>This was the argument:<br/>"{argument}"<br/><br/>That\'s the result:<br/>{output}'


if __name__ == "__main__":
    app.run(debug=True)
