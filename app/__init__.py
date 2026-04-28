import os
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from .models import db

login_manager = LoginManager()
bcryptSess = Bcrypt()

def create_app():
    app = Flask(__name__)

    #Ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    db_path = os.path.join(app.instance_path, "holoocgsite.db")

    app.config['SCRET_KEY'] = 'dev-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    bcryptSess.init_app(app)

    login_manager.login_view = 'login'

    from .routes import main_bp
    app.register_blueprint(main_bp)
    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))