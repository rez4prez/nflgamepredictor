import nflgame
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


def remove_tags(item):
    """
    Converts item to a string and removes HTML tags
    """
    item = str(item)
    item = item.replace('<', '(')
    item = item.replace('>', ')')
    item = re.sub(r" ?\([^)]+\)", "", item)
    item = item.strip()
    return item


d = {
'Away Team':[],
'Home Team':[],
'Game':[],
'Week': [],
'Year': [],
#'Date': [],
'Road Closing Spread':[],
'Home Closing Spread':[],
}
for i in range(1,18):
    url = f'https://thefootballlines.com/nfl/week-{i}/point-spreads'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    games = soup.select('td.views-field-Home-Score')
    for game in games:
        game = remove_tags(game)
        d['Game'].append(game)
        d['Week'].append(i)
    road_spread = soup.select('td.views-field-Away-Closing-Spread')
    for spread in road_spread:
        spread = remove_tags(spread)
        d['Road Closing Spread'].append(spread)
    home_spread = soup.select('td.views-field-Home-Closing-Spread')
    for spread in home_spread:
        spread = remove_tags(spread)
        d['Home Closing Spread'].append(spread)
    dates = soup.select('td.views-field-Date')
    for date in dates:
        date = remove_tags(date)
        year = ''
        for i in range(4): #only takes year from date column
            year = year + str(date[i])
        d['Year'].append(year)

#make game column comma delimtted
for game in d['Game']:
    game = game.replace(' ', ',')
    game = game.split(',')
    for i in range(0, len(game), 5):
        d['Away Team'].append(game[i])
    for i in range(3, len(game), 5):
        d['Home Team'].append(game[i])

#delete game key as we no longer need it in dataframe
del d['Game']



    


df = pd.DataFrame(d)

df.to_csv('gamelinestest2.csv')


