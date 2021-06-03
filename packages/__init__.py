from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

Env = 'dev'
if Env == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('LOCAL_POSTGRES_KEY')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('HEROKU_POSTGRES_KEY')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from .auth import auth
from .users import users

app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(auth, url_prefix='/')

# db.create_all()


@app.cli.command('init-db')
def init_db_command():
    db.create_all()
