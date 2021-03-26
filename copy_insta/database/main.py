import flask
from flask import Blueprint
from flask_login import login_required, current_user
from models import User, Pictures
from app import db
main = Blueprint('main', __name__)


def find_influencer_by_name(influencer_name):
    return User.query.filter_by(name=influencer_name).first()


@main.route('/')
def index():
    return flask.render_template('home_page.html.jinja2')


@main.route('/profile')
@login_required
def profile():
    return flask.render_template('perso_profile_page.jinja2', name=current_user.name)


@main.route('/add_photo', methods=['POST'])
@login_required
def add_photo():
    name = flask.request.form.get("photo")
    new_pic = Pictures(pic_name=name)
    db.session.add(new_pic)
    db.session.commit()


@main.route("/<name_searched>")
def profile_searched(name_searched):
    user_searched = find_influencer_by_name(name_searched)

    return flask.render_template('visitor_page.jinja2', influencer=user_searched)
