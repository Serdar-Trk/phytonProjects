import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import warnings
import datetime as dt

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

from scipy import stats
from scipy.stats import skew
from scipy.special import boxcox1p

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.exceptions import DataConversionWarning
import lightgbm as lgb
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

train = pd.read_csv('train.csv')
test = pd.read_csv('sample_submission.csv')
med = pd.read_csv('med.csv')
test0 = test.copy()
train_len = train.shape[0]
test_len = test.shape[0]


train['Tarih'] = train['Tarih'].astype('datetime64')
med['Tarih'] = med['Tarih'].astype('datetime64')

med['OVER'] = 1
train = pd.merge(train, med, how='left', on='Tarih')

train['OVER'].fillna('0', inplace=True)
train['OVER'].unique()
train['OVER'] = train['OVER'].astype(int)

print("train: ", train.shape)
print("test: ", test.shape)
print("med: ", med.shape)

ntrain = train.shape[0]
ntest = test.shape[0]

X = pd.concat([train, test], axis=0)
X.shape
X.columns = ['DATE', 'ENERGY', 'OVER']

X['DATE'] = X['DATE'].astype('datetime64')

X['HOUR'] = X['DATE'].dt.hour
X['DAY'] = X['DATE'].dt.dayofweek
X['QUARTER'] = X['DATE'].dt.quarter
X['MONTH'] = X['DATE'].dt.month
X['YEAR'] = X['DATE'].dt.year
X['DAYOFYEAR'] = X['DATE'].dt.dayofyear
X['DAYOFOMNTH'] = X['DATE'].dt.day
X['WEEKOFYEAR'] = X['DATE'].dt.weekofyear
X.head(15)

hol = pd.read_csv('Calendar.csv', parse_dates=['CALENDAR_DATE'])
hol = hol[['CALENDAR_DATE', 'RAMADAN_FLAG', 'PUBLIC_HOLIDAY_FLAG']].rename(columns={'CALENDAR_DATE': 'ds'})
hol['holiday'] = np.where((hol['RAMADAN_FLAG'] == 'Y') | (hol['PUBLIC_HOLIDAY_FLAG'] == 'Y'), 1, 0)
hol = hol[['ds', 'holiday']]
hol = hol[hol['holiday'] == 1]
hol.columns = ['DATE', 'HOLLIDAYS']

W = pd.read_csv('wind_data.csv')
W['dt'] = W['dt'].astype('datetime64')
W['DATE'] = W['dt'].rename('DATE')
W.drop('dt', axis=1, inplace=True)

W['DATE'] = W['DATE'].apply(lambda x: x.replace(year=2022) if x.year == 2017 else x)
W = W.sort_values('DATE')
W.head()

K = W.copy()
K = K.loc[K['DATE'].dt.year == 2018]
K['DATE'] = K['DATE'].apply(lambda x: x.replace(year=2021) if x.year == 2018 else x)

L = W.copy()
L = L.loc[L['DATE'].dt.year == 2019]
L['DATE'] = L['DATE'].apply(lambda x: x.replace(year=2020) if x.year == 2019 else x)

# W = pd.concat([W, A], ignore_index=True)

# A = pd.concat([L, K], join="inner", ignore_index=True)
# A=A.sort_values('DATE')

A = pd.concat([W, L, K], join="outer", ignore_index=True)
A = A.drop_duplicates()
A = A.sort_values('DATE')
A.reset_index(inplace=True)
A = A.iloc[:46056]
A.tail()
A.shape


X = pd.merge(X, hol, on='DATE', how="left")
X = pd.merge(X, A, on='DATE', how="left")
X = X.drop_duplicates()
X.isnull().sum()
# A'nin 28595 dan sonrasini kes
X[X['ENERGY'] == 0.000].shape


X['HOLLIDAYS'].fillna('0', inplace=True)
# X['HOLLIDAYS'].fillna(0,inplace=True)
X['HOLLIDAYS'] = X['HOLLIDAYS'].astype(int)

X['SPRING'] = X['DATE'].apply(lambda x: (x.month >= 3) & (x.month <= 5))
X['SUMMER'] = X['DATE'].apply(lambda x: (x.month >= 6) & (x.month <= 8))
X['AUTUMN'] = X['DATE'].apply(lambda x: (x.month >= 9) & (x.month <= 11))
X['WINTER'] = X['DATE'].apply(lambda x: (x.month >= 12) | (x.month <= 2))
X['WEEKEND'] = X['DAY'].apply(lambda x: (x == 5) | (x == 6))
X['WEEKDAY'] = ~X['DAY'].apply(lambda x: (x == 5) | (x == 6))
X['NIGHT'] = X['DATE'].apply(lambda x: (x.hour >= 0) & (x.hour <= 7))
X['WORKHOURS'] = X['DATE'].apply(lambda x: (x.hour >= 8) & (x.hour <= 19))
X['HOMEHOURS'] = X['DATE'].apply(lambda x: (x.hour >= 18) & (x.hour <= 23))
X['MORNING'] = X['DATE'].apply(lambda x: (x.hour >= 8) & (x.hour <= 12))
X['MORNING'] = X['DATE'].apply(lambda x: (x.hour >= 8) & (x.hour <= 12))
X['EVENING'] = X['DATE'].apply(lambda x: (x.hour >= 12) & (x.hour <= 17))




X.drop('index', axis=1, inplace=True)


X['DATE'].set_index()


X.head()
X.shape
X.to_csv('C:\\Users\serda\PycharmProjects\phytonProjects/gzl.csv')
