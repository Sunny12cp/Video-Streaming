import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db, auth, home, settings, create, video, contact, admin, search

    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(settings.bp)
    app.register_blueprint(create.bp)
    app.register_blueprint(video.bp)
    app.register_blueprint(contact.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(search.bp)

    app.add_url_rule("/", endpoint="index")
    app.add_url_rule("/settings", endpoint="settings")
    app.add_url_rule("/create", endpoint="create")
    app.add_url_rule("/contact", endpoint="contact")

    return app
