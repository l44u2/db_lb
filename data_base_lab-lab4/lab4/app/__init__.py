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
    
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }
    
    Swagger(app, config=swagger_config)
    
    with app.app_context():
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        db.create_all()
    
    from my_project.auth import route
    register_routes(app, route)
    
    return app

def register_routes(app, route_module):
    import inspect
    from flask import Blueprint
    
    for name, obj in inspect.getmembers(route_module):
        if isinstance(obj, Blueprint):
            app.register_blueprint(obj)
