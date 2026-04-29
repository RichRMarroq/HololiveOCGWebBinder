from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    profile = db.relationship("Profile", backref='user', uselist=False)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Core identity
    card_number = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    # Set info
    set_code = db.Column(db.String(20))
    set_name = db.Column(db.String(100))

    # Classification
    card_type = db.Column(db.String(50))   # Oshi, Holomem, Support, Cheer
    rarity = db.Column(db.String(20))

    # Color (2 max for now)
    color_1 = db.Column(db.String(20))
    color_2 = db.Column(db.String(20))

    # Media
    image_url = db.Column(db.String(255))
    artist = db.Column(db.String(100))

    # Stats (only some apply depending on type)
    life = db.Column(db.Float)   # Oshi
    hp = db.Column(db.Float)     # Holomem
    stage = db.Column(db.String(50))  # Debut, Spot, etc.

    # Support-specific
    support_type = db.Column(db.String(50))
    is_limited = db.Column(db.Boolean)

    # Text
    effect_text = db.Column(db.Text)

    def __repr__(self):
        return f"<Card {self.card_number} - {self.name}>"

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    bio = db.Column(db.Text)
    avatar_image = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)