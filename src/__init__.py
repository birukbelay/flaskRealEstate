from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import get_config

migrate = Migrate()

db = SQLAlchemy()


def create_app(config_name):
    app = Flask("house rental system")
    app.config.from_object(get_config(config_name))

    from src.api.auth_api import auth
    from src.api.user_api import users

    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(auth, url_prefix='/')

    db.init_app(app)
    migrate.init_app(app, db)
    return app



# db.create_all()
