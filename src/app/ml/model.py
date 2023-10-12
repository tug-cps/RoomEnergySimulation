import os

import joblib
import pandas as pd

absolute_path = os.path.dirname(__file__)


def load_model():
    model_path = os.path.join(absolute_path, "linear_model_6_features.pkl")
    return joblib.load(model_path)


def predict(X: pd.DataFrame):
    model = load_model()
    return model.predict(X)
