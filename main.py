from YHandler import YHandler, YQuery
from pprint import pprint

def get_standings():
    ns = {'yh': 'http://fantasysports.yahooapis.com/fantasy/v2/base.rng'}

    handler = YHandler()
    query = YQuery(handler, 'nhl')

    league = query.get_user_leagues()[0]

    #print league['name'], league['id']

    standings = query.query_league(league['id'], "standings")

    result = []
    for team in standings.iter_select('.//yh:teams/yh:team', ns):
        result.append(
            team.select_one('./yh:name', ns).text
        )
    '''result.append({
        'id': league.select_one('./yh:league_id', ns).text,
        'name': league.select_one('./yh:name', ns).text,
        'season': league.select_one('./yh:season', ns).text,
        'week': league.select_one('./yh:current_week', ns).text,
        'is_finished': (lambda val: True if val else False)(league.select_one('./yh:is_finished', ns).text)
     })'''

    #print result
    #pprint(standings)
    return result

print get_standings()
