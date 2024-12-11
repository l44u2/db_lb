# my_project/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()

def create_app(app_config: dict) -> Flask:
    app = Flask(__name__)
    app.config.update(app_config)
    db.init_app(app)
    with app.app_context():
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        db.create_all()
    return app