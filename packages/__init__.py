from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

Env = 'dev'
if Env == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:54123@localhost:5432/books_review"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://rygzpgaazcnyyb:ea7fe9df1881379cf43397a997b5f6d5c740b034b8c20afd5fe61f45199c2053@ec2-3-215-57-87.compute-1.amazonaws.com:5432/d842t2f117c8dc"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from .auth import auth
from .users import users

app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(auth, url_prefix='/')

# db.create_all()


@app.cli.command('init-db')
def init_db_command():
    db.create_all()
