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
from players import teams
import urllib2
import re
from lxml import etree
import xml.etree.ElementTree as ElementTree
"""

Refer: https://docs.python.org/2/library/json.html

filename = open('../Models/team_players.json', 'r')

read_file = filename.read()

y=json.loads(read_file)
"""
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', -1)
players = []
players_info = []
live_games = []
player_stats = {'gp':None,'w':None,'l':None,'win_pct':None,'min':None,'fgm':None,'fga':None,'fg_pct':None,
                'fg3m':None,'fg3a':None,'fg3_pct':None,'ftm':None,'fta':None,'ft_pct':None,'oreb':None,'dreb':None,
                'reb':None,'ast':None,'tov':None,'stl':None,'blk':None,'pf':None,'pts':None,'plus_minus':None}
player_common_info = {'first_name':None,'last_name':None,'jersey':None,'position':None,'team':None,'experience':None,
                      'school':None,'height':None,'weight':None,'birthdate':None}
play_by_play_info = {'quarter':None,'time':None,'home':None,'away':None}
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


def get_live_scores():
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_1.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_1.xml'
            content = urllib2.urlopen(url).read()   
            quarter1 = etree.fromstring(content)
            for event in quarter1.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '1', 'TIME': val, 'EVENT': s})
    except: 
        print 'DNE'
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_2.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_2.xml'
            content = urllib2.urlopen(url).read()   
            quarter2 = etree.fromstring(content)
            for event in quarter2.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '2', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_3.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_3.xml'
            content = urllib2.urlopen(url).read()   
            quarter3 = etree.fromstring(content)
            for event in quarter3.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '3', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_4.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_4.xml'
            content = urllib2.urlopen(url).read()   
            quarter4 = etree.fromstring(content)
            for event in quarter4.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '4', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_5.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_5.xml'
            content = urllib2.urlopen(url).read()   
            quarter4 = etree.fromstring(content)
            for event in quarter4.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': 'OT', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_6.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_6.xml'
            content = urllib2.urlopen(url).read()   
            quarter4 = etree.fromstring(content)
            for event in quarter4.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '2OT', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_7.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/20150301/GSWBOS/pbp_7.xml'
            content = urllib2.urlopen(url).read()   
            quarter4 = etree.fromstring(content)
            for event in quarter4.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '3OT', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    """play_by_play = response.xml()['resultSets'][0]['rowSet']
    data = simplejson.loads(response.text)
    headers = data['resultSets'][0]['headers']
    game_data = data['resultSets'][0]['rowSet']
    play_by_play_df = pd.DataFrame(game_data,columns=headers)
    quarter = play_by_play_df['PERIOD'].to_string()
    time = play_by_play_df['PCTIMESTRING'].to_string()
    home = play_by_play_df['HOMEDESCRIPTION'].to_string()
    away = play_by_play_df['VISITORDESCRIPTION'].to_string()
    play_by_play_info['quarter'] = quarter
    play_by_play_info['time'] = time
    play_by_play_info['home'] = home
    play_by_play_info['away'] = away
    live_games.append(play_by_play_info.copy())"""
    


def scores():
    get_live_scores()
    live_games_cols = ['QUARTER', 'TIME', 'EVENT']
    live_games_df = pd.DataFrame(live_games,columns = live_games_cols)
    live_games_df = live_games_df.to_html(classes="table table-condensed", index=False)
    return dict(live_games_df=live_games_df)


def team_players():
    return(dict(a="a"))

def player_info(player_id):
    url = 'http://stats.nba.com/stats/commonplayerinfo?LeagueID=00&' + \
    'PlayerID='+player_id+'&SeasonType=Regular+Season'
    response = requests.get(url)
    shots = response.json()['resultSets'][0]['rowSet']
    data = simplejson.loads(response.text)
    headers = data['resultSets'][0]['headers']
    shot_data = data['resultSets'][0]['rowSet']
    player_info_df = pd.DataFrame(shot_data,columns=headers)
    first_name = player_info_df['FIRST_NAME'].to_string()
    last_name = player_info_df['LAST_NAME'].to_string()
    jersey = player_info_df['JERSEY'].mean(axis=1)
    position = player_info_df['POSITION'].to_string()
    team = player_info_df['TEAM_NAME'].to_string()
    experience = player_info_df['SEASON_EXP'].mean(axis=1)
    school = player_info_df['SCHOOL'].to_string()
    height = player_info_df['HEIGHT'].to_string()
    weight= player_info_df['WEIGHT'].mean(axis=1)
    birthdate = player_info_df['BIRTHDATE'].to_string()
    player_common_info['first_name'] = first_name
    player_common_info['last_name'] = last_name
    player_common_info['jersey'] = jersey
    player_common_info['position'] = position
    player_common_info['team'] = team
    player_common_info['experience'] = experience
    player_common_info['school'] = school
    player_common_info['height'] = height
    player_common_info['weight'] = weight
    player_common_info['birthdate'] = birthdate
    players_info.append(player_common_info.copy())
    print player_common_info

def find_current_stats(player_id):
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
    #print response.elapsed
    shots = response.json()['resultSets'][0]['rowSet']
    data = simplejson.loads(response.text)
    #print ('================================')
    #print data
    #Create df from data and find averages
    headers = data['resultSets'][0]['headers']
    shot_data = data['resultSets'][0]['rowSet']
    reg_stats_df = pd.DataFrame(shot_data,columns=headers)
    #print ('+++++++++++++++++++++++++++++++++')
    #print df
    """avg_def = df['CLOSE_DEF_DIST'].mean(axis=1)
    avg_dribbles = df['DRIBBLES'].mean(axis=1)
    avg_shot_distance = df['SHOT_DIST'].mean(axis=1)
    avg_touch_time = df['TOUCH_TIME'].mean(axis=1)"""
    gp = reg_stats_df['GP'].mean(axis=1)
    w = reg_stats_df['W'].mean(axis=1)
    l = reg_stats_df['L'].mean(axis=1)
    win_pct = reg_stats_df['W_PCT'].mean(axis=1)
    min = reg_stats_df['MIN'].mean(axis=1)
    fgm = reg_stats_df['FGM'].mean(axis=1)
    fga = reg_stats_df['FGA'].mean(axis=1)
    fg_pct = reg_stats_df['FG_PCT'].mean(axis=1)
    fg3m = reg_stats_df['FG3M'].mean(axis=1)
    fg3a = reg_stats_df['FG3A'].mean(axis=1)
    fg3_pct = reg_stats_df['FG3_PCT'].mean(axis=1)
    ftm = reg_stats_df['FTM'].mean(axis=1)
    fta = reg_stats_df['FTA'].mean(axis=1)
    ft_pct = reg_stats_df['FT_PCT'].mean(axis=1)
    oreb = reg_stats_df['OREB'].mean(axis=1)
    dreb = reg_stats_df['DREB'].mean(axis=1)
    reb = reg_stats_df['REB'].mean(axis=1)
    ast = reg_stats_df['AST'].mean(axis=1)
    tov = reg_stats_df['TOV'].mean(axis=1)
    stl = reg_stats_df['STL'].mean(axis=1)
    blk = reg_stats_df['BLK'].mean(axis=1)
    pf = reg_stats_df['PF'].mean(axis=1)
    pts = reg_stats_df['PTS'].mean(axis=1)
    plus_minus = reg_stats_df['PLUS_MINUS'].mean(axis=1)
    #add averages to dictionary
    #player_stats['name'] = name
    """player_stats['avg_defender_distance']=avg_def
    player_stats['avg_shot_distance'] = avg_shot_distance
    player_stats['avg_touch_time'] = avg_touch_time
    player_stats['avg_dribbles'] = avg_dribbles
    players.append(player_stats.copy())"""
    player_stats['gp'] = gp
    player_stats['w']= w
    player_stats['l'] = l
    player_stats['win_pct'] = win_pct
    player_stats['min'] = min
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

def view():
    p = db.player(request.args(0))
    find_current_stats(p.player_id)
    player_info(p.player_id)
    player_info_cols = ['first_name','last_name','jersey','position','team','experience',
                      'school','height','weight','birthdate']
    reg_stats_cols = ['gp', 'w', 'l', 'win_pct', 'min', 'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a', 'fg3_pct',
            'ftm', 'fta','ft_pct', 'pf', 'oreb', 'dreb', 'reb', 'ast', 'tov', 'stl', 'blk', 'pts', '+/-']
    player_info_df = pd.DataFrame(players_info, columns = player_info_cols)
    player_info_df = player_info_df.to_html(classes="table table-condensed",index=False)
    #print player_info_df
    reg_stats_df = pd.DataFrame(players,columns = reg_stats_cols)
    reg_stats_df = reg_stats_df.to_html(classes="table table-condensed", index=False)
    return dict(player_info_df=player_info_df,reg_stats_df=reg_stats_df)

def stats():
    with open ('applications/ballislife/static/team_players.json') as f:
        data=f.read()
        z=simplejson.dumps(data)
    q = db.player
    #NBA Stats API using selected player ID
    """Will continue inserting into db.player
    for x in teams:
        for y,z in teams[x].items():
            db.player.insert(**{'name':y, 'player_id':z, 'team':x})"""
    #print db.executesql('DELETE (*) FROM player;')
    #print db.executesql('SELECT * FROM player;')
        #for y in teams[x]:
            #db.player.insert(**{})
            #print teams[x][y]
    def generate_view_button(row):
        view_page = A('View', _class='btn', _href=URL('default', 'view', args=[row.id]))
        return view_page
    links = [
        dict(header='', body = generate_view_button),
        ]
    form = SQLFORM.grid(q,
        fields=[db.player.name, db.player.team],csv=False, orderby=db.player.name, details=False, links=links)
    """find_stats('Stephen Curry','201939')
    #find_stats('James Harden','201935')
    #find_stats('Klay Thompson','202691')
    #find_stats('LeBron James','2544')
    #cols = ['name','avg_defender_distance','avg_dribbles','avg_shot_distance','avg_touch_time']
    cols = ['name', 'gp', 'w', 'l', 'win_pct', 'min', 'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a', 'fg3_pct',
            'ftm', 'fta','ft_pct', 'pf', 'oreb', 'dreb', 'reb', 'ast', 'tov', 'stl', 'blk', 'pts', '+/-']
    df = pd.DataFrame(players,columns = cols)
    print ('=========================')
    print df
    df = df.to_html(classes="table table-condensed")"""
    return dict(form=form)

def top_players():
    df = pd.read_json('http://stats.nba.com/stats/homepagev2?GameScope=Season&LeagueID=00&PlayerOrTeam=Player&PlayerScope=All+Players&Season=2014-15&SeasonType=Regular+Season&StatType=Traditional')
    df[['created_at', 'title', 'body', 'comments']]
    print df
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
