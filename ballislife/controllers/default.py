# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################
import requests
import json as simplejson
import pandas as pd

"""

Refer: https://docs.python.org/2/library/json.html

filename = open('../Models/team_players.json', 'r')

read_file = filename.read()

y=json.loads(read_file)
"""
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', -1)
players = []
player_stats = {'name':None,'games':None,'wins':None,'losses':None,'win_pct':None,'minutes':None,'fgm':None,'fga':None,'fg_pct':None,
                'fg3m':None,'fg3a':None,'fg3_pct':None,'ftm':None,'fta':None,'ft_pct':None,'oreb':None,'dreb':None,'reb':None,'ast':None,
                'tov':None,'stl':None,'blk':None,'pf':None,'pts':None,'plus_minus':None}
#player_stats = {'name':None,'avg_dribbles':None,'avg_touch_time':None,'avg_shot_distance':None,'avg_defender_distance':None}

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    test = 'My Thumbnail'
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


def scores():
    test = 'My Thumbnail'
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def team_players():
    return(dict(a="a"))

def find_stats(name,player_id):
    """url = 'http://stats.nba.com/stats/playerdashptshotlog?'+ \
    'DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&' + \
    'Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&' + \
    'PlayerID='+player_id+'&Season=2014-15&SeasonSegment=&' + \
    'SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision='"""
    
    url = 'http://stats.nba.com/stats/playerdashboardbygeneralsplits?' + \
    'DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&' + \
    'MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&' + \
    'PerMode=PerGame&Period=0&PlayerID='+player_id+'+&PlusMinus=N&Rank=N' + \
    '&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&VsConference=&VsDivision='
    
    #Create Dict based on JSON response
    response = requests.get(url)
    shots = response.json()['resultSets'][0]['rowSet']
    data = simplejson.loads(response.text)
    #print ('================================')
    #print data
    #Create df from data and find averages
    headers = data['resultSets'][0]['headers']
    shot_data = data['resultSets'][0]['rowSet']
    df = pd.DataFrame(shot_data,columns=headers)
    #print ('+++++++++++++++++++++++++++++++++')
    #print df
    """avg_def = df['CLOSE_DEF_DIST'].mean(axis=1)
    avg_dribbles = df['DRIBBLES'].mean(axis=1)
    avg_shot_distance = df['SHOT_DIST'].mean(axis=1)
    avg_touch_time = df['TOUCH_TIME'].mean(axis=1)"""
    games = df['GP'].mean(axis=1)
    wins = df['W'].mean(axis=1)
    losses = df['L'].mean(axis=1)
    win_pct = df['W_PCT'].mean(axis=1)
    minutes = df['MIN'].mean(axis=1)
    fgm = df['FGM'].mean(axis=1)
    fga = df['FGA'].mean(axis=1)
    fg_pct = df['FG_PCT'].mean(axis=1)
    fg3m = df['FG3M'].mean(axis=1)
    fg3a = df['FG3A'].mean(axis=1)
    fg3_pct = df['FG3_PCT'].mean(axis=1)
    ftm = df['FTM'].mean(axis=1)
    fta = df['FTA'].mean(axis=1)
    ft_pct = df['FT_PCT'].mean(axis=1)
    oreb = df['OREB'].mean(axis=1)
    dreb = df['DREB'].mean(axis=1)
    reb = df['REB'].mean(axis=1)
    ast = df['AST'].mean(axis=1)
    tov = df['TOV'].mean(axis=1)
    stl = df['STL'].mean(axis=1)
    blk = df['BLK'].mean(axis=1)
    pf = df['PF'].mean(axis=1)
    pts = df['PTS'].mean(axis=1)
    plus_minus = df['PLUS_MINUS'].mean(axis=1)
    #add averages to dictionary
    player_stats['name'] = name
    """player_stats['avg_defender_distance']=avg_def
    player_stats['avg_shot_distance'] = avg_shot_distance
    player_stats['avg_touch_time'] = avg_touch_time
    player_stats['avg_dribbles'] = avg_dribbles
    players.append(player_stats.copy())"""
    player_stats['games'] = games
    player_stats['wins']= wins
    player_stats['losses'] = losses
    player_stats['win_pct'] = win_pct
    player_stats['minutes'] = minutes
    player_stats['fgm'] = fgm
    player_stats['fga'] = fga
    player_stats['fg_pct'] = fg_pct
    player_stats['fg3m'] = fg3m
    player_stats['fg3a'] = fg3a
    player_stats['fg3_pct'] = fg3_pct
    player_stats['ftm'] = ftm
    player_stats['fta'] = fta
    player_stats['ft_pct'] = ft_pct
    player_stats['ftm'] = ftm
    player_stats['fta'] = fta
    player_stats['ft_pct'] = ft_pct
    player_stats['oreb'] = oreb
    player_stats['dreb'] = dreb
    player_stats['reb'] = reb
    player_stats['ast'] = ast
    player_stats['tov'] = tov
    player_stats['stl'] = stl
    player_stats['blk'] = blk
    player_stats['pf'] = pf
    player_stats['pts'] = pts
    player_stats['+/-'] = plus_minus
    players.append(player_stats.copy())

def stats():
    with open ('applications/ballislife/static/team_players.json') as f:
        data=f.read()
        z=simplejson.dumps(data)
    #NBA Stats API using selected player ID
    #for x in teams:
    #    for y in teams[x]:
    #        find_stats(y,teams[x][y])
    find_stats('stephen curry','201939')
    find_stats('james harden','201935')
    #cols = ['name','avg_defender_distance','avg_dribbles','avg_shot_distance','avg_touch_time']
    cols = ['name', 'games', 'wins', 'losses', 'win_pct', 'minutes', 'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a', 'fg3_pct',
            'ftm', 'fta','ft_pct', 'pf', 'oreb', 'dreb', 'reb', 'ast', 'tov', 'stl', 'blk', 'pts', '+/-']
    #
    df = pd.DataFrame(players,columns = cols)
    print ('=========================')
    print df
    df = df.to_html()
    return dict(df=df)

def top_players():
    test = 'My Thumbnail'
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
