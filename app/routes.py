from flask import Blueprint
from flask import render_template

main_bp = Blueprint('main',__name__)

NAVIGATION = [
    {"href": "/", "caption": "Home"},
    {"href": "/decks", "caption": "Decks"},
    {"href": "/cards", "caption": "Cards"},
    {"href": "/about", "caption": "About"}
]

@main_bp.route('/')
def index():
    pageName = "Home"
    return render_template('base.html.jinja', title=pageName, navigation=NAVIGATION, a_variable="This is a variable passed from the route to the template.")

@main_bp.route('/decks')
def decks():
    pageName = "Decks"
    return render_template('base.html.jinja', title=pageName, navigation=NAVIGATION, a_variable="This is a variable passed from the route to the template.")

@main_bp.route('/cards')
def cards():
    pageName = "Cards"
    return render_template('base.html.jinja', title=pageName, navigation=NAVIGATION, a_variable="This is a variable passed from the route to the template.")

@main_bp.route('/about')
def about():
    pageName = "About"
    return render_template('base.html.jinja', title=pageName, navigation=NAVIGATION, a_variable="This is a variable passed from the route to the template.")