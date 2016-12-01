import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from standings import get_standings


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_game():
    welcome_msg = "Here are the standings for your fantasy league: "
    for name in get_standings():
        welcome_msg += name + ", "
    return statement(welcome_msg)

@ask.intent("YesIntent")
def next_round():
    numbers = [randint(0, 9) for _ in range(3)]
    round_msg = render_template('round', numbers=numbers)
    session.attributes['numbers'] = numbers[::-1]  # reverse
    return question(round_msg)

@ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})
def answer(first, second, third):
    winning_numbers = session.attributes['numbers']
    if [first, second, third] == winning_numbers:
        msg = render_template('win')
    else:
        msg = render_template('lose')
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)
