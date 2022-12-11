from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from app import login
from flask_login import UserMixin

user_favorite = db.Table('favorites',
                         db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                         db.Column('message_id', db.Integer, db.ForeignKey('message.id'), primary_key=True)
                         )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(32), unique=True)
    messages = db.relationship('Message', backref='user', lazy=True)
    favorite_messages = db.relationship('Message', secondary=user_favorite, lazy='subquery',
                                        backref=db.backref('users_who_favorite', lazy=True))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.String(250))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<User {self.user}, {self.contents}>'
