from fastapi import FastAPI
import pandas as pd

app = FastAPI()

g = pd.read_csv('games_final.csv')


#1
@app.get('/genero/{year}')
def genero(year: str):
    genero = g[g.year == year]
    d = genero[[
        'Action', 'Indie', 'Adventure', 'Casual', 'Fighting', 'Indie',
        'Free to Play', 'Great Soundtrack', 'Multiplayer', 'Puzzle', 'RPG',
        'Sandbox', 'Shooter', 'Simulation', 'Singleplayer', 'Sports',
        'Strategy', 'Survival', 'Zombies'
    ]].sum().sort_values(ascending=False).head(10).to_dict()
    return d


#2


@app.get('/juegos/{year}')
def juegos(year: str):
    dicc = g.groupby([
        'year'
    ])['title'].count().sort_values(ascending=False).head(10).to_dict()
    return dicc[year]


#3


@app.get('/spec/{year}')
def spec(year: str):
    specs = g[g.year == year]
    d = specs[[
        'Single-player', 'Steam Achievements', 'Downloadable Content',
        'Steam Trading Cards', 'Steam Cloud', 'Multi-player',
        'Full controller support', 'Partial Controller Support',
        'Steam Leaderboards', 'Co-op', 'Shared/Split Screen'
    ]].sum().sort_values(ascending=False).iloc[:5].to_dict()
    return d


#4


@app.get('/earlyacces/{year}')
def earlyacces(year: str):
    ea = g[['year', 'early_access']]
    return ea[(ea.year == year) & (ea.early_access == 1)].shape[0]


#5


@app.get('/sentiment/{year}')
def sentiment(year: str):
    sent = g[['year', 'sentiment']]
    d = sent[sent.year == year]['sentiment'].value_counts().head().to_dict()
    return d


#6
@app.get('/metascore/{year}')
def metascore(year: str):
    score = g[['year', 'metascore']]
    return score[score.year == year]['metascore'].sort_values(
        ascending=False).head().to_list()
