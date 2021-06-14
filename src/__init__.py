from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import get_config

migrate = Migrate()

db = SQLAlchemy()


def create_app(config_name):
    app = Flask("house rental system")
    app.config.from_object(get_config(config_name))

    from src.rest import api_bp
    app.register_blueprint(api_bp, url_prefix='/')

    db.init_app(app)
    migrate.init_app(app, db)

    return app

# db.create_all()
