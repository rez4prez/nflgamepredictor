#import datacollection
import numpy
import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.feature_selection import RFE
import pandas as pd

nflgames = pd.read_csv('nflfull.csv')
#nflgames = datacollection.merge_full()
new = nflgames[['Home Win?','Week', 'Home PF', 'Home PA','Home Wins to Date','Home Losses to Date','Home Ties to Date', 'Away PF','Away PA','Away Wins to Date', 
    'Away Losses to Date', 'Away Ties to Date', 'Road Closing Spread', 'Home Closing Spread']]
x = new.drop('Home Win?', 1) #Feature Matrix
y = new['Home Win?']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
#x_train = preprocessing.scale(x_train)
logmodel = LogisticRegression()
rfe = RFE(logmodel, 6)
fit = rfe.fit(x, y)
print("Num Features: %s" % (fit.n_features_))
print("Selected Features: %s" % (fit.support_))
print("Feature Ranking: %s" % (fit.ranking_))
print(x)

# logmodel.fit(x_train, y_train)
# predictions = logmodel.predict(x_test)
# print(classification_report(y_test, predictions))
# print(confusion_matrix(y_test, predictions))
# print(accuracy_score(y_test, predictions))

# score = logmodel.score(x_test, y_test)
# print(score)
# print(predictions)
