from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from models import User
from app import db
import flask

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return flask.render_template('login.html.jinja2')


@auth.route('/login', methods=['POST'])
def login_post():
    email = flask.request.form.get('email')
    password = flask.request.form.get('password')
    remember = True if flask.request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flask.flash('Please check your login details and try again.')
        return flask.redirect(flask.url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return flask.redirect(flask.url_for('main.profile'))


@auth.route('/signup')
def signup():
    return flask.render_template('signup.html.jinja2')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = flask.request.form.get('email')
    name = flask.request.form.get('name')
    password = flask.request.form.get('password')

    user = User.query.filter_by(email=email).first()  # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flask.flash('This email address already exists')
        return flask.redirect(flask.url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return flask.redirect(flask.url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for('main.index'))
