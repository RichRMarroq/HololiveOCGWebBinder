from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, User, Card, Profile, Deck, Deck_Card
from . import bcryptSess
from flask_login import login_user, logout_user, login_required, current_user

main_bp = Blueprint('main',__name__)


@main_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        hashed_pw = bcryptSess.generate_password_hash(
            request.form.get('password')
        ).decode('utf-8')

        user = User(
            username=request.form.get('username'),
            email=request.form.get('email'),
            password_hash=hashed_pw
        )

        profile = Profile(
            username=request.form.get('username'),
            user=user
        )

        db.session.add(user)
        db.session.commit()
        print(f"User Created: {request.form.get('username')}\nPass: {request.form.get('password')}")

        return redirect(url_for('main.login'))
    return render_template('register.html.jinja')

@main_bp.route('/')
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("Attempting Login")
        user = User.query.filter_by(
            email=request.form.get('email')
        ).first()
        
        if user:
            print("Found User")
            print(request.form.get('password'))
            print(f"Password Matches?: {bcryptSess.check_password_hash(
            user.password_hash,
            request.form.get('password')
        )}")

        if user and bcryptSess.check_password_hash(
            user.password_hash,
            request.form.get('password')
        ):
            login_user(user)
            print("User Logged In")
            return redirect(url_for('main.home'))
    return render_template('login.html.jinja')

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main_bp.route('/home')
@login_required
def home():
    #Display User Decks
    decks = Deck.query.filter_by(profile_id=current_user.id).limit(3)
    
    return render_template('home.html.jinja', decks=decks)

@main_bp.route('/decks')
@login_required
def decks():
    return render_template('decks.html.jinja')

@main_bp.route('/cards')
@login_required
def cards():
    card_type = request.args.get('type')

    query = Card.query

    if card_type:
        query = query.filter_by(card_type=card_type)
    
    cards = query.order_by(Card.card_number).all()
    return render_template('cards.html.jinja', cards=cards, selected_type=card_type)

@main_bp.route('/about')
@login_required
def about():
    user_id = current_user.id
    return render_template('about.html.jinja', user_id=user_id)

@main_bp.route('/create_deck', methods = ['POST'])
@login_required
def create_deck():
    user_id = current_user.id
    query = Profile.query

    profile = query.filter_by(user_id=user_id).first()
    deck = Deck(
            deck_name=request.form.get('deck_name'),
            profile_id=profile.id
        )

    db.session.add(deck)
    db.session.commit()
    return redirect(url_for('main.home'))

