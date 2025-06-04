from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/home')
def hello1():
    return 'Welcome to My Watchlist!'

from markupsafe import escape

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'