import requests
usrl="https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
targetcsv='orders.csv'
response=requests.get(url=usrl)
response.raise_for_status()
with open('targetcsv','wb')as f:
    f.write(response.content)
