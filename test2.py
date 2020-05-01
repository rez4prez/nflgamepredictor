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


d = {'Game':[],
'Week': [],
# 'Year': []
#'Date': [],
'Road Closing Spread':[],
'Home Closing Spread':[],
}
for i in range(1,18):
    url = f'https://thefootballlines.com/nfl/week-{i}/point-spreads'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    games = soup.select('.dataTables_info')
    for game in games:
        game = remove_tags(game)
        print(games)