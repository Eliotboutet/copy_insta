from flask_login import UserMixin
from app import db, pictures


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Pictures(UserMixin, pictures.Model):
    id = pictures.Column(pictures.Integer, primary_key=True)
    who_posted = pictures.Column(pictures.Integer)
    keywords = pictures.Column(pictures.String(2000))
    likes = pictures.Column(pictures.Integer)
    comments = pictures.Column(pictures.TEXT)
    photo = pictures.Column(pictures.BLOB)
