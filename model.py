import joblib
import json


def my_simple_model(argument):
    """A dummy model, returning the length of the input argument."""
    result = len(argument)
    return result


def my_real_model(argument):
    """A dummy model, returning the length of the input argument."""
    model = joblib.load("mymodel.pkl")
    argument_array = [json.loads(argument)]
    result = model.predict(argument_array)
    # result = len(argument)
    return result
