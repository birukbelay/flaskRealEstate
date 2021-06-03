from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

Env = 'de'
uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

if Env == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('LOCAL_POSTGRES_KEY')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from .auth import auth
from .users import users

app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(auth, url_prefix='/')

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "server error"
    }),
# db.create_all()


@app.cli.command('init-db')
def init_db_command():
    db.create_all()

@app.cli.command('reclean-db')
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()