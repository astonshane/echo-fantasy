import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from yahoo import get_standings, get_league


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def welcome():
    welcome_msg = "Welcome to your fantasy hockey app! What stats do you want to hear?"
    #welcome_msg = "Here are the standings for your fantasy league: "
    '''for name in get_standings():
        welcome_msg += name + ", "'''
    return question(welcome_msg)

@ask.intent("StandingsIntent")
def standings():
    league = get_league()
    msg = "Here are the standings for the {name} fantasy {sport} league: ".format(name=league['name'], sport=league['sport'])
    msg += ', '.join(get_standings())
    msg += ". " + "What stats do you want to hear next?"
    return question(msg)

@ask.intent("HelpIntent")
def help():
    options = [
        "List Standings",
        "Some other option",
        "A third option",
        "Done"
    ]

    help_msg = "I can give you any of the following information: "
    help_msg += ', '.join(options) + ". "
    help_msg += "What stats do you want to hear?"
    return(question(help_msg))

@ask.intent("ExitIntent")
def exit():
    msg = "Thanks for listening!"
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)
