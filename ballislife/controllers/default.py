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
from lxml import etree
import time

live_games = []

def index():
    """Get parameters for current date to pass into url"""
    day = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%Y')
    url = 'http://stats.nba.com/scores/#!/' + month + '/' + day + '/' + year
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'}
    """Get results from response at NBA.com to obtain standings for Eastern and Western Conference"""
    with requests.Session() as session:
        session.headers = headers
        session.get(url, headers=headers)

        params = {
            'DayOffset': '0',
            'GameDate': month + '/' + day + '/' + year,
            'LeagueID': '00'
        }
    
        response = session.get('http://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate='+month+'%2F'+day+'%2F'+year, params=params)
        results = response.json()
        eastHeaders = results['resultSets'][4]['headers']
        eastRows = results['resultSets'][4]['rowSet']
        westHeaders = results['resultSets'][5]['headers']
        westRows = results['resultSets'][5]['rowSet']
    return dict(eastHeaders=eastHeaders,eastRows=eastRows,westHeaders=westHeaders,westRows=westRows)

def game_info():
    """get parameters from scores view to pass into get_live_scores()"""
    arg1 = request.args(0)
    arg2 = request.args(1)
    """Check to see if play by play data is returned, otherwise, print 'No Info Found'"""
    try:
        get_live_scores(arg1, arg2)
        live_games_cols = ['QUARTER', 'TIME', 'EVENT']
        live_games_df = pd.DataFrame(live_games,columns = live_games_cols)
        live_games_df = live_games_df.to_html(classes="table table-condensed", index=False)
        return dict(live_games_df=live_games_df, arg1=arg1, arg2=arg2)
    except:
        live_games_df = 'No Info Found'
        return dict(live_games_df=live_games_df, arg1=arg1, arg2=arg2)

def get_live_scores(team1, team2):
    """Get parameters for current date to pass into url"""
    day = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%Y')
    """Check to see if xml file for quarterly play by play data is available, else print 'DNE' to log"""
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_1.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_1.xml'
            content = urllib2.urlopen(url).read()   
            quarter1 = etree.fromstring(content)
            for event in quarter1.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '1', 'TIME': val, 'EVENT': s})
    except: 
        print 'DNE'
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_2.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_2.xml'
            content = urllib2.urlopen(url).read()   
            quarter2 = etree.fromstring(content)
            for event in quarter2.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '2', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_3.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_3.xml'
            content = urllib2.urlopen(url).read()   
            quarter3 = etree.fromstring(content)
            for event in quarter3.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '3', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_4.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_4.xml'
            content = urllib2.urlopen(url).read()   
            quarter4 = etree.fromstring(content)
            for event in quarter4.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '4', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    """Check to see if xml file for overtime (up to 3OT) play by play data is available, else print 'DNE' to log"""
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_5.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_5.xml'
            content = urllib2.urlopen(url).read()   
            quarter4 = etree.fromstring(content)
            for event in quarter4.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': 'OT', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_6.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_6.xml'
            content = urllib2.urlopen(url).read()   
            quarter4 = etree.fromstring(content)
            for event in quarter4.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '2OT', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    try: 
        if (urllib2.urlopen('http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_7.xml').getcode() == 200):
            url = 'http://data.nba.com/data/5s/xml/nbacom/2014/scores/'+year+month+day+'/'+team1+team2+'/pbp_7.xml'
            content = urllib2.urlopen(url).read()   
            quarter4 = etree.fromstring(content)
            for event in quarter4.xpath("//event"):
                s = event.text
                val = s.split('(', 1)[1].split(')')[0]
                live_games.append({'QUARTER': '3OT', 'TIME': val, 'EVENT': event.text})
    except: 
        print 'DNE'
    
    
def scores():
    """Get parameters for current date to pass into url"""
    day = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%Y')
    url = 'http://stats.nba.com/scores/#!/' + month + '/' + day + '/' + year
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'}
    """Get results from response at NBA.com to obtain simple boxscore for daily games"""
    with requests.Session() as session:
        session.headers = headers
        session.get(url, headers=headers)

        params = {
            'DayOffset': '0',
            'GameDate': month + '/' + day + '/' + year,
            'LeagueID': '00'
        }
        response = session.get('http://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate='+month+'%2F'+day+'%2F'+year, params=params)
        results = response.json()
        headers = results['resultSets'][1]['headers']
        rows = results['resultSets'][1]['rowSet']
    return dict(headers=headers, rows=rows)

    
def team_stats():
    url = "http://stats.nba.com/league/team/#!/advanced/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'}
    """Get results from response at NBA.com to obtain stats for each team"""
    with requests.Session() as session:
        session.headers = headers
        session.get(url, headers=headers)

        params = {
            'DateFrom': '',
            'DateTo': '',
            'GameScope': '',
            'GameSegment': '',
            'LastNGames': '0',
            'LeagueID': '00',
            'Location': '',
            'MeasureType': 'Advanced',
            'Month': '0',
            'OpponentTeamID': '0',
            'Outcome': '',
            'PaceAdjust': 'N',
            'PerMode': 'Totals',
            'Period': '0',
            'PlayerExperience': '',
            'PlayerPosition': '',
            'PlusMinus': 'N',
            'Rank': 'N',
            'Season': '2014-15',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'VsConference': '',
            'VsDivision': ''
        }
    
        response = session.get('http://stats.nba.com/stats/leaguedashteamstats', params=params)
        results = response.json()
        headers = results['resultSets'][0]['headers']
        rows = results['resultSets'][0]['rowSet']
    return dict(headers=headers, rows=rows)
        

def view():
    """Get player from database"""
    p = db.player(request.args(0))
    url = 'http://stats.nba.com/player/#!/' + p.player_id + '/stats/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'}
    """Get results from response at NBA.com to obtain stats and info for selected player"""
    with requests.Session() as session:
        session.headers = headers
        session.get(url, headers=headers)

        params = {
            'DateFrom': '',
            'DateTo': '',
            'GameSegment': '',
            'LastNGames': '0',
            'LeagueID': '00',
            'Location': '',
            'MeasureType': 'Base',
            'Month': '0',
            'OpponentTeamID': '0',
            'Outcome': '',
            'PaceAdjust': 'N',
            'PerMode': 'PerGame',
            'Period': '0',
            'PlayerID': p.player_id,
            'PlusMinus': 'N',
            'Rank': 'N',
            'Season': '2014-15',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'VsConference': '',
            'VsDivision': ''
        }
    
        response = session.get('http://stats.nba.com/stats/playerdashboardbygeneralsplits?DateFrom=&DateTo=&GameSegment=' + 
                               '&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&' + 
                               'PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID='+ p.player_id + '&PlusMinus=N&Rank=N&Season=2014-15&' + 
                               'SeasonSegment=&SeasonType=Regular+Season&VsConference=&VsDivision=', params=params)
        results = response.json()
        headers = results['resultSets'][0]['headers']
        rows = results['resultSets'][0]['rowSet']
        
        params = {
            'PlayerID': p.player_id,
            'LeagueID': '00'
        }
    
        response = session.get('http://stats.nba.com/stats/commonplayerinfo?LeagueID=00&PlayerID='+p.player_id+'&SeasonType=Regular+Season', params=params)
        results = response.json()
        infoHeaders = results['resultSets'][0]['headers']
        infoRows = results['resultSets'][0]['rowSet']
        name = p.name
    return dict(headers=headers, rows=rows,infoHeaders=infoHeaders,infoRows=infoRows, name=name)

def player_stats():
    """Get player from database"""
    q = db.player
    """Will continue inserting into db.player
    for x in teams:
        for y,z in teams[x].items():
            db.player.insert(**{'name':y, 'player_id':z, 'team':x})"""
    """Create button to view player from SQLFORM"""
    def generate_view_button(row):
        view_page = A('View', _class='btn', _href=URL('default', 'view', args=[row.id]))
        return view_page
    links = [
        dict(header='', body = generate_view_button),
        ]
    """Create SQLFORM with list of all players"""
    form = SQLFORM.grid(q,
        fields=[db.player.name, db.player.team],csv=False, orderby=db.player.name, details=False, links=links)
    return dict(form=form)

def stats():
    test = 'My Thumbnail'
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


def top_players():
    url = "http://stats.nba.com/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'}
    """Get results from response at NBA.com to obtain top 5 players for main stats"""
    with requests.Session() as session:
        session.headers = headers
        session.get(url, headers=headers)

        params = {
            'GameScope': 'Season',
            'LeagueID': '00',
            'PlayerOrTeam': 'Player',
            'PlayerScope': 'All Players',
            'Season': '2014-15',
            'SeasonType': 'Regular Season',
            'StatType': 'Traditional'
        }
    
        response = session.get('http://stats.nba.com/stats/homepagev2?GameScope=Season&LeagueID=00&PlayerOrTeam=Player' + 
                               '&PlayerScope=All+Players&Season=2014-15&SeasonType=Regular+Season&StatType=Traditional', params=params)
        results = response.json()
        pointHeaders = results['resultSets'][0]['headers']
        pointRows = results['resultSets'][0]['rowSet']
        reboundHeaders = results['resultSets'][1]['headers']
        reboundRows = results['resultSets'][1]['rowSet']
        assistHeaders = results['resultSets'][2]['headers']
        assistRows = results['resultSets'][2]['rowSet']
        stealHeaders = results['resultSets'][3]['headers']
        stealRows = results['resultSets'][3]['rowSet']
        fgHeaders = results['resultSets'][4]['headers']
        fgRows = results['resultSets'][4]['rowSet']
        ftHeaders = results['resultSets'][5]['headers']
        ftRows = results['resultSets'][5]['rowSet']
        threePtHeaders = results['resultSets'][6]['headers']
        threePtRows = results['resultSets'][6]['rowSet']
        blockHeaders = results['resultSets'][7]['headers']
        blockRows = results['resultSets'][7]['rowSet']
    return dict(pointHeaders=pointHeaders,pointRows=pointRows,reboundHeaders=reboundHeaders,reboundRows=reboundRows,
                assistHeaders=assistHeaders,assistRows=assistRows,stealHeaders=stealHeaders,stealRows=stealRows,
                fgHeaders=fgHeaders,fgRows=fgRows,ftHeaders=ftHeaders,ftRows=ftRows,threePtHeaders=threePtHeaders,
                threePtRows=threePtRows,blockHeaders=blockHeaders,blockRows=blockRows)

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
