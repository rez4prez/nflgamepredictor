#!python
import nflgame
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

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

DF = correct_weeks()
DF.to_csv('correctweeks.csv')