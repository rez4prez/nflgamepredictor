#!python
import nflgame
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def nflgames_2010_to_2019():
    """
    Returns a dataframe containing general information pertaining to all regualr season NFL games from 2010-2019
    """

    data = {
    'Home Win?':[],
    'Away Win?':[],
    'Score Differential':[],
    'Year':[],
    'Week':[],
    'Home Team':[],
    'Away Team':[],
    'Score Home':[],
    'Score Away':[]}

    for x in range(2010, 2020):
        for z in range(1,18):
            try:
                games = nflgame.games(x, week=z)
                for i in range(len(games)):
                    data['Year'].append(x)
                    data['Week'].append(z)
                    data['Home Team'].append(games[i].home) 
                    data['Away Team'].append(games[i].away)
                    data['Score Home'].append(games[i].score_home)
                    data['Score Away'].append(games[i].score_away)
                    if data['Score Home'][i] > data['Score Away'][i]:
                        data['Home Win?'].append(1)
                        data['Away Win?'].append(0)
                    elif data['Score Home'][i] < data['Score Away'][i]:
                        data['Home Win?'].append(0)
                        data['Away Win?'].append(1)
                    else:
                        data['Home Win?'].append(0)
                        data['Away Win?'].append(0)
                    data['Score Differential'].append(abs(data['Score Home'][i] - data['Score Away'][i]))
            except:
                pass #if an error occurs (ie. a certain week within a season has no game data for some reason, it will do nothing and skip to next iteration)
    for n, i in enumerate(data['Home Team']):
        if i == 'JAX':
            data['Home Team'][n] = 'JAC'
    for n, i in enumerate(data['Away Team']):
        if i == 'JAX':
            data['Away Team'][n] = 'JAC'

    df = pd.DataFrame(data)
    return(df)


def pf_winlosses():
    points_data = {
    'Year':[],
    'Week':[],
    'Team':[],
    'PF':[],
    'PA':[],
    'Wins to Date':[],
    'Losses to Date':[],
    'Ties':[]}

    teams = []
    for i in nflgame.teams:
        teams.append(i[0])
    teams.append('JAX') #after 2015 the abbreviation from nflgames changes from JAC to JAX

    for team in teams:
        for x in range(2010, 2020):
            points_for = 0
            points_against = 0
            wins = 0
            losses = 0
            ties = 0
            for z in range(2,19):
                try:
                    games = nflgame.games(x, week=z-1, home=team, away=team, kind='REG', started=False)
                    for i in range(len(games)): #pretty sure this statement is unnecssary cause were singling out a single game 
                        if games[i].home == team:
                            points_for = points_for + games[i].score_home
                            points_against = points_against + games[i].score_away
                            if games[i].score_home > games[i].score_away:
                                wins += 1
                            elif games[i].score_home == games[i].score_away:
                                ties += 1
                            else:
                                losses += 1
                        else:
                            points_for = points_for + games[i].score_away
                            points_against = points_against + games[i].score_home
                            if games[i].score_away > games[i].score_home:
                                wins += 1
                            elif games[i].score_home == games[i].score_away:
                                ties += 1
                            else:
                                losses += 1
                        points_data['Year'].append(x)
                        points_data['Week'].append(z)
                        points_data['Team'].append(team)
                        points_data['PF'].append(points_for)
                        points_data['PA'].append(points_against)
                        points_data['Wins to Date'].append(wins)
                        points_data['Losses to Date'].append(losses)
                        points_data['Ties'].append(ties)
                except:
                    pass

    for n, i in enumerate(points_data['Team']):
        if i == 'JAX':
            points_data['Team'][n] = 'JAC'

    return(points_data)


def correct_weeks():
    """
    Handles the edge cases where Byes messed up week numbers
    """
    points_data = pf_winlosses()
    weeks = points_data['Week']
    try:
        for i in range(len(weeks)):
            first = weeks[i + 1]
            second = weeks[i]
            difference = first - second
            if difference == 2:
                weeks[i] += 1
    except:
        pass
    points_data['Week'] = weeks
    df = pd.DataFrame(points_data)
    return(df)


def merge_initial():
    d1 = nflgames_2010_to_2019()
    d2 = correct_weeks()
    new = pd.merge(d1, d2, how='left', left_on = ['Year', 'Week', 'Home Team'], right_on = ['Year', 'Week', 'Team'])
    new = new.rename(columns={'PF': 'Home PF', 'PA': 'Home PA', 'Wins to Date': 'Home Wins to Date', 'Losses to Date': 'Home Losses to Date', 'Ties': 'Home Ties to Date'})
    new2 = pd.merge(new, d2, how='left', left_on = ['Year', 'Week', 'Away Team'], right_on = ['Year', 'Week', 'Team'])    
    new2 = new2.rename(columns={'PF': 'Away PF', 'PA': 'Away PA', 'Wins to Date': 'Away Wins to Date', 'Losses to Date': 'Away Losses to Date', 'Ties': 'Away Ties to Date'})
    return new2

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

def gamelines():
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
            year = int(year)
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
    d = pd.DataFrame(d)
    #d.to_csv("gamelines.csv") # have to go in and edit incorrect years and replace LAR abbreviation with LA


def merge_full():
    d1 = merge_initial()
    d2 = pd.read_csv('gamelines.csv')
    new = pd.merge(d1, d2, how='left', left_on = ['Year', 'Week', 'Home Team'], right_on = ['Year', 'Week', 'Home Team'])
    new.fillna(0, inplace=True)
    new = new.drop(columns=['Team_x', 'Team_y', 'Unnamed: 0', 'Away Team_y' ])
    new = new.drop_duplicates()
    return new


df = merge_full()
df.to_csv("nflfull.csv")

    




