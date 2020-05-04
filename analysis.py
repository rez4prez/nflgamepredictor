from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import roc_auc_score
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.preprocessing import StandardScaler

nflgames = pd.read_csv('nflfull.csv')
new = nflgames[['Home Win?', 'Home PF', 'Home PA', 'Home Wins to Date', 'Home Losses to Date', 'Home Ties to Date ', 'Away PF', 'Away PA', 'Away Wins to Date',
                'Away Losses to Date', 'Away Ties to Date ', 'Road Closing Spread', 'Home Closing Spread']]
x = new.drop('Home Win?', 1)  # Feature Matrix
y = new['Home Win?']  # target variable
print(x.isnull().sum())  # no missing values in any of the columns
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0)
print(x_train.shape, x_test.shape)  # shows shape of train and test set

### Step Forward Feature Selection ###
sfs = SFS(RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1),
          k_features=(1, 12),
          forward=True,
          floating=False,
          verbose=2,
          scoring='accuracy',
          cv=4,
          n_jobs=-1).fit(x_train, y_train)

print(f'\n {sfs.k_feature_names_}, {sfs.k_score_}')

### Step Backward Feature Selection ###
sfs = SFS(RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1),
          k_features=(1, 12),
          forward=False,
          floating=False,
          verbose=2,
          scoring='accuracy',
          cv=4,
          n_jobs=-1).fit(x_train, y_train)

print(f'\n {sfs.k_feature_names_}, {sfs.k_score_}')

### Exhaustive Feature Selection ###
efs = EFS(RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1),
          min_features=4,
          max_features=5,
          scoring='accuracy',
          cv=None,
          n_jobs=-1).fit(x_train, y_train)

print(f'\n {efs.best_feature_names_}, {efs.best_score_}')
