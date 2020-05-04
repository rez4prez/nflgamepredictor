from flask import render_template, Flask, request, redirect
import requests  # used requests package instead because it is bettter
import json
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import roc_auc_score
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['GET', 'POST'])
def generate_prediction():
    if request.method == 'POST':
        nflgames = pd.read_csv('nflfull.csv')
        new = nflgames[['Home Win?', 'Home PF', 'Home PA',
                        'Home Wins to Date', 'Road Closing Spread']]
        x = new.drop('Home Win?', 1)  # Feature Matrix
        y = new['Home Win?']  # target variable
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2, random_state=0)
        model = RandomForestClassifier(
            n_estimators=100, random_state=0, n_jobs=-1).fit(x_train, y_train)
        user_input = {'Home PF': [], 'Home PA': [],
                      'Home Wins to Date': [], 'Road Closing Spread': []}
        user_input['Home PF'] = [request.form['Home PF']]
        user_input['Home PA'] = [request.form['Home PA']]
        user_input['Home Wins to Date'] = [request.form['Home Wins to Date']]
        user_input['Road Closing Spread'] = [
            request.form['Road Closing Spread']]
        user_input_df = pd.DataFrame(user_input)
        y_pred = model.predict(user_input_df)
        home_team = request.form['Home Team']
        away_team = request.form['Away Team']
        if y_pred == 1:
            return render_template('predictions.html', winning_team=home_team)
        else:
            return render_template('predictions.html', winning_team=away_team)


@app.errorhandler(Exception)
# handles all exceptions
def error404(error):
    return render_template('error.html', explanation='You must provide input for all fields')