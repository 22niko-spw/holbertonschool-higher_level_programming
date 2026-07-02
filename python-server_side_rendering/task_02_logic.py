#!/usr/bin/python3
"""Application Flask affichant une liste d'items chargée depuis JSON."""
import json
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


@app.route('/items')
def items():
    """Affiche la liste des items lue depuis items.json."""
    with open('items.json') as f:
        data = json.load(f)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
