import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database import models
from database.database import db, init_database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Insta.sqlite3'
db.init_app(app)

with app.app_context():
    init_database()


def get_all_engineers():
    return models.Engineer.query.all()


def get_influencer_by_username(influencer_username):
    return models.Engineer.query.filter_by(username=influencer_username).first()


@app.route('/engineers')
def hello_world():
    influencers = get_all_engineers()
    result = "All influencers:\n"
    for influencer in influencers:
        result += " - %s (username:%s)\n" % (influencer.id, influencer.username)
    return flask.Response(result,
                          mimetype="text")


@app.route('/')
def first_boot():
    influencers = get_all_engineers()
    result = "All influencers:\n"
    for influencer in influencers:
        result += " - %s (username:%s)\n" % (influencer.id, influencer.username)
    return flask.render_template("home_page.html.jinja2",
                                 influencers=influencers)


@app.route('/<string:influencer_username>')
def profil(influencer_username):
    influencer = get_influencer_by_username(influencer_username)
    return flask.render_template("profile_page.jinja2",
                                influencer=influencer)


if __name__ == Flask('__main__'):
    app.run()
