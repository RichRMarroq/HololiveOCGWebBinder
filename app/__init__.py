from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
bcryptSess = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SCRET_KEY'] = 'dev-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///holoocgsite.db'

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcryptSess.init_app(app)

    login_manager.login_view = 'login'

    from .routes import main_bp
    app.register_blueprint(main_bp)
    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))