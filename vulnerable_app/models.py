from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email    = db.Column(db.String(120), nullable=False)
    ssn_last4= db.Column(db.String(4), nullable=False)
    role     = db.Column(db.String(20), default="user")

class Order(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    item    = db.Column(db.String(100))
    total   = db.Column(db.Float)

class Document(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    title    = db.Column(db.String(100))
    content  = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Profile(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    user_id  = db.Column(db.Integer, db.ForeignKey("user.id"))
    bio      = db.Column(db.Text)
    role     = db.Column(db.String(20), default="user")
