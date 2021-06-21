import joblib

from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge


X, y = load_diabetes(return_X_y = True)

model = Ridge().fit(X, y)

joblib.dump(model, 'mymodel.pkl')
