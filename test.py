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
new = nflgames[['Home Win?', 'Home PF', 'Home PA',
                'Home Wins to Date', 'Road Closing Spread']]
x = new.drop('Home Win?', 1)  # Feature Matrix
y = new['Home Win?']  # target variable
print(x.isnull().sum())  # no missing values in any of the columns
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0)
model = RandomForestClassifier(
    n_estimators=100, random_state=0, n_jobs=-1).fit(x_train, y_train)
print(x_test)
d = {'Home PF': [48], 'Home PA': [63],
     'Home Wins to Date': [5], 'Road Closing Spread': [5]}
df = pd.DataFrame(d)
new_test = pd.concat([x_test, df])
print(new_test)
y_pred = model.predict(new_test)
print(y_pred)

y_pred = model.predict(x)
y_pred = list(y_pred)
predictions = dict()
predictions['predictions'] = y_pred
print(predictions)

new['Predictions'] = predictions['predictions']
print(new)

new.to_csv("nflpredictionsmodel.csv")

correct = 0
for i in range(len(new['Home Win?'])):
    if new['Home Win?'][i] == new['Predictions'][i]:
        correct += 1

accuracy = correct / len(new['Home Win?'])
print(accuracy)
