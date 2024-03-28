from flask_sqlalchemy import SQLAlchemy
import sqlite3


db = SQLAlchemy()

def create_db_tables():
    conn = sqlite3.connect('restaurant.db')

    with open('schema.sql') as f:
        conn.executescript(f.read())

create_db_tables()        