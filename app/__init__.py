import os
from flask import Flask, render_template
from .database import db
from .short import short

def get_database_uri():
    uri = os.environ.get('DATABASE_URL')
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    return uri


class ServerConfig(object):
    DEBUG = os.environ.get('DEBUG', default=False)
    TESTING = os.environ.get('TESTING', default=False)
    SECRET_KEY = "p3s6v9y$B&E)H+MbQeThWmZq4t7w!z%C*F-JaNcRfUjXn2r5u8x/A?D(G+KbPeSg"
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.environ.get('DEBUG', default=False)

def setup_server():
    app = Flask(__name__)
    app.config.from_object(ServerConfig)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(short)

    return app
