#!/usr/bin/python3
"""Application Flask basique : sert des pages HTML via Jinja."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Page d'accueil."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Page About."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Page Contact."""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
