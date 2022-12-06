from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from app import login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(32), unique=True)
    messages = db.relationship('Message', backref='user', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.String(250))
    like_count = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'<User {self.user}, {self.contents}>'
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
