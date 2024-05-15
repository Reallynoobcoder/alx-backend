#!/usr/bin/env python3
"""A basic Flask app."""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """Configure available languages in our app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """A function with the babel.localeselector decorator."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """Render template for index.html page."""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
