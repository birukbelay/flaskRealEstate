from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:54123@localhost:5432/books_review"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from .auth import auth
from .users import users

app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(auth, url_prefix='/')

db.create_all()


@app.cli.command('init-db')
def init_db_command():
    db.create_all()
