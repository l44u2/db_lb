import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flasgger import Swagger

db = SQLAlchemy()

def create_app(app_config: dict, additional_config: dict = None) -> Flask:
    app = Flask(__name__)
    app.config.update(app_config)
    if additional_config:
        app.config.update(additional_config)
    
    db.init_app(app)
    
    Swagger(app, template={
        "info": {
            "title": "Event Management API",
            "description": "API for managing events, animators, agencies",
            "version": "1.0.0"
        }
    })
    
    with app.app_context():
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        db.create_all()
    
    from my_project.auth.route import register_routes
    register_routes(app)
    
    return app
