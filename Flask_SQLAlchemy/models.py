# This allows a user to log in and make notes.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model): # Database conection
    id = db.Column(db.Integer, primary_key=True) # how to map from a database table in a python instance.
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    notes = db.relationship('Note', backref='author', lazy=True)  # Lazy means it won't fetch all the notes

# User omitted
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # DOn't want notes that doesn't have a user.  There has to be a user to have a ID