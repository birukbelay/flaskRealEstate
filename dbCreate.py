import os

from flask import Flask, render_template, request
from src.models.user import *
from src.models.houses import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:54123@localhost:5432/houses"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()