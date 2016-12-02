from YHandler import YHandler, YQuery
from pprint import pprint

ns = {'yh': 'http://fantasysports.yahooapis.com/fantasy/v2/base.rng'}

def get_standings():

    handler = YHandler()
    query = YQuery(handler, 'nhl')

    league = query.get_user_leagues()[0]

    standings = query.query_league(league['id'], "standings")

    result = []
    for team in standings.iter_select('.//yh:teams/yh:team', ns):
        result.append(
            team.select_one('./yh:name', ns).text
        )

    return result

def get_league():
    handler = YHandler()
    query = YQuery(handler, 'nhl')

    league = query.get_user_leagues()[0]

    standings = query.query_league(league['id'], "standings")

    resp = {}
    resp['sport'] = "hockey"
    resp['name'] = league['name']

    return resp

print get_league()
