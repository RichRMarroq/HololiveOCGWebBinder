from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    from app.models import User
    db.create_all()
    print("Database created!")