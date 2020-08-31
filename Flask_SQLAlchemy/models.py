# This allows a user to log in and make notes.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model): # Database conection
    id = db.Column(db.Integer, primary_key=True) # how to map from a database table in a python instance.
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())