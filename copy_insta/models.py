from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Pictures(UserMixin, db.Model):
    __tablename__='pictures'
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    who_posted = db.Column(db.Interval, nullable=False)
    likes = db.Column(db.Integer)
    comments = db.Column(db.TEXT)
