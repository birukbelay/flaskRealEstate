from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
app.config["DEBUG"] = True

Env = 'de'
uri = os.getenv("DATABASE_URL", "")
print("uri:--",uri)
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

if Env == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('LOCAL_POSTGRES_KEY')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from packages.api.auth import auth
from packages.api.user import users

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
