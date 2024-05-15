from . import db, Rol
from sqlalchemy import SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(255))
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), default=2)
    status = db.Column(SmallInteger, nullable=True, default=1)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

    rol = db.relationship('Rol', backref=db.backref('users', lazy=True))

    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email

    def verify_password(self, password):
        return check_password_hash(self.password, password)
