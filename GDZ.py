import pandas as pd
# !pip install pmdarima
# !pip install workalendar
# !pip install prophet
# !pip install -q --upgrade linear-tree

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import warnings
import datetime as dt

# from joblib import Parallel, delayed
# from time import sleep, time
# import logging


# import itertools
# import holidays
# import keras


# import pmdarima as pm
# import requests
# import statsmodels
# import statsmodels.tsa.api as sm
# import tensorflow as tf
import xgboost as xgb
# from keras import backend as K
# from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
# from keras.models import Sequential
# from keras.layers import Dense, LSTM, Activation, Dropout
# from lineartree import LinearBoostRegressor
# from matplotlib import rcParams  # Used to set default paremeters
# from prophet import Prophet
# from prophet.diagnostics import cross_validation
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
# from sklearn.preprocessing import MinMaxScaler
# from statsmodels.graphics.tsaplots import month_plot, plot_acf, plot_pacf, quarter_plot
# from workalendar.europe import UnitedKingdom
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler

# ---------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns
import pylab

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 140)

X = pd.read_csv('X (1).csv')

X.head()

X.set_index('DATE', inplace=True)

threshold_date_1 = "2022-01-01"
threshold_date_2 = "2022-08-01"
train = X.loc[X.index < threshold_date_1]
test = X.loc[(X.index >= threshold_date_1) & (X.index < threshold_date_2)]
hold_out = X.loc[X.index >= threshold_date_2]

X_hold_out = hold_out.drop(['ENERGY'], axis=1)
y_hold_out = hold_out['ENERGY']

X_train = train.drop(['ENERGY'], axis=1)
y_train = train['ENERGY']

X_test = test.drop(['ENERGY'], axis=1)
y_test = test['ENERGY']

print("X_train:", len(X_train))
print("X_test:", len(X_test))
print("y_train:", len(y_train))
print("y_test:", len(y_test))

train.index = pd.Index(train.index)
test.index = pd.Index(test.index)

# FEATURES = ['HOUR', 'DAY', 'QUARTER', 'YEAR', 'HOLLIDAYS', 'TEMP', 'SPRING', 'SUMMER','AUTUMN',
#        'WINTER','WORKHOURS', 'MORNING', 'EVENING', 'ROLLING_MEAN_T41', 'ROLLING_MEAN_T48',
#        'ROLLING_MEAN_T168', 'ROLLING_MEAN_T1', 'ROLLING_MEAN_T50', 'ROLLING_MEAN_T99', 'ROLLING_MEAN_T88', 'ROLLING_MEAN_T77',
#        'ROLLING_MEAN_T80', 'ROLLING_STD_T38', 'QUARTER2']


# TARGET = "ENERGY"

# # Define train, test and hold-out set for the cv features
# X_train_cv = train[FEATURES]
# y_train_cv = train[TARGET]

# X_test_cv = test[FEATURES]
# y_test_cv = test[TARGET]


# X_hold_out = hold_out[FEATURES]
# y_hold_out = hold_out[TARGET]


X_train_cv = X_train
y_train_cv = y_train

X_test_cv = X_test
y_test_cv = y_test



# Define fit parameters to allow early stopping in GridSearchCV
fit_params = {
    #     "early_stopping_rounds": 50,
    # "eval_metric": "rmse",
    "eval_set": [[X_hold_out, y_hold_out]],
}

# Define estimator
estimator = xgb.XGBRegressor(
    base_score=0.5,
    booster="gbtree",
    learning_rate=0.01,
    tree_method="gpu_hist",
    random_state=43,
)

# Define parameters to optimiser
param_search = {
    "max_depth": range(1, 11),
    "n_estimators": [700, 800, 900, 1000],
    "subsample": [0.8, 0.7, 0.6],
    #     "min_samples_split": range(2, 20),
}

# Create GridSearchCV object
xgb_search = GridSearchCV(
    estimator=estimator,
    cv=5,
    param_grid=param_search,
    n_jobs=-1,
    verbose=1,
).fit(X_train_cv, y_train_cv, **fit_params)

xgb_search.best_params_
