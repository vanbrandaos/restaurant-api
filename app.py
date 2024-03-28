from flask import Flask
import sqlite3

from controller import api
from db import db
from ma import ma

#create server

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'

db.init_app(app)


# with app.app_context() as ctx:
#     ctx.push()
#     db.create_all()

# @app.before_request
# def create_tables():
#     db.create_all()

ma.init_app(app)
api.init_app(app)

HOST = "0.0.0.0"
PORT = 5000 

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)