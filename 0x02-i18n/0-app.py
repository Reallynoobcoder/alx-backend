#!/usr/bin/env python3
"""A basic Flask app."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render template for index.html page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)