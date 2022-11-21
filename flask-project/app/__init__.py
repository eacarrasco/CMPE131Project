from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.update(
	SECRET_KEY=b"idkwhateveriwant123",
	SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db')
)

db = SQLAlchemy(myapp_obj)

from app import routes
