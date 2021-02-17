import flask

app = flask.Flask(__name__)


@app.route('/')
def first_boot():
    return flask.render_template("template_bootstrap1.jinja2")


if __name__ == '__main__':
    app.run()
