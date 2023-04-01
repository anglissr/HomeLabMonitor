from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ip = db.Column(db.String(100))
    running = db.Column(db.Boolean, default=True)
    app1 = db.Column(db.String(100))
    app2 = db.Column(db.String(100))
    app3 = db.Column(db.String(100))
    app4 = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('devices', lazy=True))