import flask
from flask import Blueprint
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return flask.render_template('home_page.html.jinja2')


@main.route('/profile')
@login_required
def profile():
    return flask.render_template('profile_temporary.html.jinja2', name=current_user.name)
