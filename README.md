# Example API

This is a small example API code, using the Python `flask` framework.

## Run it

Start it with

```bash
# install dependencies
pipenv install

# run the code
pipenv shell
python app.py
```

## Useful tags

* `v0`: provides a static endpoint returning "hello world" </br> http://127.0.0.1:5000/

* `v1`: adds a dynamic endpoint returning a random number [0-1] </br> http://127.0.0.1:5000/random

* `v2`: extends the random endpoint with the option to add a number </br> http://127.0.0.1:5000/random/plus?input=2

* `v3`: adds a simple dummy model endpoint returning the length of the argument </br> http://127.0.0.1:5000/model?input=2

* `v4`: adds proper error handling and HTTP return codes

* `v5`: adds the trained model on the textbook diabetes dataset from the `.pkl` file and returns the hospitalization score </br> http://127.0.0.1:5000/diabetes?input=[-0.00188201652779104, -0.044641636506989, -0.0514740612388061, -0.0263278347173518, -0.00844872411121698, -0.019163339748222, 0.0744115640787594, -0.0394933828740919, -0.0683297436244215, -0.09220404962683]
