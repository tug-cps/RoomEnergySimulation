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
import joblib
import os


def train(data, model_path):
    
    # Split the training data into inputs and outputs
    inputs = data[['insulation_thickness', 'u_values']]
    outputs = data['annual_energy_use']

    dt_reg_grid = {
        'criterion': ['mse', 'friedman_mse'],
        'splitter': ['best', 'random'],
        'max_depth': [None, 2, 4, 6, 8, 10],
        'min_samples_split': [2, 4, 6, 8, 10],
        'min_samples_leaf': [1, 2, 4, 6, 8, 10],
    }


    # Define the decision tree regression model
    dt_reg = DecisionTreeRegressor()

    # Use grid search to find the best parameters for the linear regression model
    dt_reg_grid_search = GridSearchCV(dt_reg, dt_reg_grid, cv=5, scoring='neg_mean_squared_error')
    dt_reg_grid_search.fit(inputs, outputs)
    
    # Serialize and save the model
    joblib.dump(dt_reg_grid_search.best_estimator_, model_path)