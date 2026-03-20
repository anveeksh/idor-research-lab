"""
seed_data.py — Populate the SQLite DB with fake test data using Faker.
Run this once before starting the app.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, User, Order, Document, Profile
from faker import Faker

fake = Faker()

def seed():
    with app.app_context():
        db.create_all()

        # Clear existing data
        Profile.query.delete()
        Document.query.delete()
        Order.query.delete()
        User.query.delete()
        db.session.commit()

        users = []
        for i in range(10):
            u = User(
                username  = fake.user_name(),
                email     = fake.email(),
                ssn_last4 = fake.numerify("####"),
                role      = "admin" if i == 0 else "user"
            )
            db.session.add(u)
            users.append(u)
        db.session.commit()

        for u in users:
            # One order per user
            db.session.add(Order(
                user_id = u.id,
                item    = fake.word(),
                total   = round(fake.random_number(digits=3) / 10, 2)
            ))
            # One document per user
            db.session.add(Document(
                title    = fake.sentence(nb_words=4),
                content  = fake.paragraph(),
                owner_id = u.id
            ))
            # One profile per user
            db.session.add(Profile(
                user_id = u.id,
                bio     = fake.sentence(),
                role    = "admin" if u.role == "admin" else "user"
            ))

        db.session.commit()
        print(f"✅ Seeded {len(users)} users, orders, documents, and profiles.")

if __name__ == "__main__":
    seed()
