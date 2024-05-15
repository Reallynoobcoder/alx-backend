#!/usr/bin/env python3
"""A basic Flask app."""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """Configure available languages in our app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@babel.localeselector
def get_locale() -> str:
    """A function with the babel.localeselector decorator."""
    locale = request.args.get('locale')
    print(locale)
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user(user_id) -> dict:
    '''Return user dictionary based on user ID'''
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None

@app.before_request
def before_request():
    """Execute before all other functions."""
    user_id = request.args.get('user_id')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None

@app.route('/')
def home():
    """Render template for index.html page."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
