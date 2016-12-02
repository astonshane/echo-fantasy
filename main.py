import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from yahoo import get_standings, get_league


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_game():
    welcome_msg = "Welcome to your fantasy hockey app! What stats do you want to hear?"
    #welcome_msg = "Here are the standings for your fantasy league: "
    '''for name in get_standings():
        welcome_msg += name + ", "'''
    return question(welcome_msg)

@ask.intent("StandingsIntent")
def next_round():
    league = get_league()
    msg = "Here are the standings for the {name} fantasy {sport} league: ".format(name=league['name'], sport=league['sport'])
    msg += ', '.join(get_standings())
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)
