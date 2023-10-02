from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt
import math
import pickle
import os

from .model import train


if __name__ == "__main__":
    path_to_data = Path(__file__).parent.parent.joinpath("data").joinpath("preproccesed.csv")
    df = pd.read_csv(path_to_data)
    
    path_to_models = Path(__file__).parent.parent.joinpath("models").joinpath("dt_reg_model.pkl")
    train(df, str(path_to_models))