
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database import models
from database.database import db, init_database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Insta.sqlite3'
db.init_app(app)


with app.app_context():
    init_database()


@app.route('/')
def hello_world():
    engineers = get_all_engineers()
    return engineers.email


def get_all_engineers():
    return models.Engineer.query.filter_by(username='ezraa').first()


if __name__ == '__main__':
    app.run()
