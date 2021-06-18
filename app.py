from flask import Flask, request

import random


app = Flask(__name__)



@app.route("/")
def home():
    return 'Hello Back Belt Course!'


@app.route("/random/")
def random_number():
    number = random.random()
    return f'Your random number: {number}'


@app.route("/random/plus")
def random_number_plus():
    argument = request.args.get('plus')
    try:
        number = random.random() + float(argument)
        return f'Your random number plus {argument}: {number}'
    except ValueError:
        return f'Your argument has to be a number! ({argument} is an invalid argument)', 400


if __name__ == "__main__":
    app.run(debug=True)
