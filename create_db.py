from app import create_app
from app.models import db, User, Card

app = create_app()

with app.app_context():
    db.create_all()
    print("Database created!")
    print(db.metadata.tables)