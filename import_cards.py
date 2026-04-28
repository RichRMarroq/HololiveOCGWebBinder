import csv
from app import create_app
from app.models import db, Card

app = create_app()

def parse_bool(value):
    if value is None:
        return None
    return str(value).strip().lower() in ["true", "1", "yes"]

def parse_float(value):
    try:
        return float(value) if value not in (None, "", "NaN") else None
    except:
        return None

with app.app_context():
    with open('docs\data\csvData\cards.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Skip duplicates
            if Card.query.filter_by(card_number=row['card_number']).first():
                continue

            card = Card(
                id=int(row['card_id']) if row.get('card_id') else None,
                card_number=row['card_number'],
                name=row['name'],

                set_code=row.get('set_code'),
                set_name=row.get('set_name'),

                card_type=row.get('card_type'),
                rarity=row.get('rarity'),

                color_1=row.get('color_1'),
                color_2=row.get('color_2'),

                image_url=row.get('image_url'),
                artist=row.get('artist'),

                life=parse_float(row.get('life')),
                hp=parse_float(row.get('hp')),
                stage=row.get('stage'),

                support_type=row.get('support_type'),
                is_limited=parse_bool(row.get('is_limited')),

                effect_text=row.get('effect_text')
            )

            db.session.add(card)

        db.session.commit()

    print("Cards imported successfully!")