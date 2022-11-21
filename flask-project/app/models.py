from app import db


class User:
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String(200))
    email = db.Column(db.String(64), unique=True)
