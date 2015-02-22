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

players = []
player_stats = {'name':None,'avg_dribbles':None,'avg_touch_time':None,'avg_shot_distance':None,'avg_defender_distance':None}

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
    url = 'http://stats.nba.com/stats/playerdashptshotlog?'+ \
    'DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&' + \
    'Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&' + \
    'PlayerID='+player_id+'&Season=2014-15&SeasonSegment=&' + \
    'SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision='
    
    #Create Dict based on JSON response
    response = requests.get(url)
    shots = response.json()['resultSets'][0]['rowSet']
    data = simplejson.loads(response.text)
    print ('_______________________________')
    print data
    print ('-------------------------------')
    #Create df from data and find averages 
    headers = data['resultSets'][0]['headers']
    shot_data = data['resultSets'][0]['rowSet']
    df = pd.DataFrame(shot_data,columns=headers) 
    avg_def = df['CLOSE_DEF_DIST'].mean(axis=1)
    avg_dribbles = df['DRIBBLES'].mean(axis=1)
    avg_shot_distance = df['SHOT_DIST'].mean(axis=1)
    avg_touch_time = df['TOUCH_TIME'].mean(axis=1)
     
    #add averages to dictionary
    player_stats['name'] = name
    player_stats['avg_defender_distance']=avg_def
    player_stats['avg_shot_distance'] = avg_shot_distance
    player_stats['avg_touch_time'] = avg_touch_time
    player_stats['avg_dribbles'] = avg_dribbles
    players.append(player_stats.copy())

def stats():
    with open ('applications/ballislife/static/team_players.json') as f:
        data=f.read()
        z=simplejson.dumps(data)
    #NBA Stats API using selected player ID
    #for x in teams:
    #    for y in teams[x]:
    #        find_stats(y,teams[x][y])
    find_stats('stephen curry','201939');
    cols = ['name','avg_defender_distance','avg_dribbles','avg_shot_distance','avg_touch_time']
    df = pd.DataFrame(players,columns = cols)
    print ('=========================')
    print df
    df.head()
    return dict(df=df);

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
