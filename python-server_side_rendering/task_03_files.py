#!/usr/bin/python3
"""Application Flask affichant des produits depuis JSON ou CSV,
avec filtrage optionnel par id et gestion des erreurs."""
import csv
import json
from flask import Flask, render_template, request

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


def read_json():
    """Lit et retourne la liste de produits depuis products.json."""
    with open('products.json') as f:
        return json.load(f)


def read_csv():
    """Lit et retourne la liste de produits depuis products.csv.

    Convertit id en int et price en float pour un format homogène
    avec la lecture JSON.
    """
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
    return products


@app.route('/products')
def products():
    """Affiche les produits filtrés selon les query params
    'source' (json|csv) et 'id' (optionnel)."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error="Product not found"
            )

        product = next((p for p in data if p['id'] == product_id), None)
        if product is None:
            return render_template(
                'product_display.html', error="Product not found"
            )
        return render_template('product_display.html', products=[product])

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
