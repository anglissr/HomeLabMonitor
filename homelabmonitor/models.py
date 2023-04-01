from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    key = db.Column(db.String(200))
    api = db.Column(db.String(100))
    # add other columns for the service details

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ip = db.Column(db.String(100))
    running = db.Column(db.Boolean, default=True)
    service1_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    service1 = db.relationship('Service', backref='service1_devices', foreign_keys=[service1_id])
    service2_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    service2 = db.relationship('Service', backref='service2_devices', foreign_keys=[service2_id])
    service3_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    service3 = db.relationship('Service', backref='service3_devices', foreign_keys=[service3_id])
    service4_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    service4 = db.relationship('Service', backref='service4_devices', foreign_keys=[service4_id])
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('devices', lazy=True))