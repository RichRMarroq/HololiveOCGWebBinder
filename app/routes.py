from flask import Blueprint
from flask import render_template

main_bp = Blueprint('main',__name__)

@main_bp.route('/')
def index():
    return render_template('home.html.jinja')

@main_bp.route('/decks')
def decks():
    return render_template('decks.html.jinja')

@main_bp.route('/cards')
def cards():
    return render_template('cards.html.jinja')

@main_bp.route('/about')
def about():
    return render_template('about.html.jinja')