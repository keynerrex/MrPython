from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import SmallInteger, BigInteger
from werkzeug.security import (generate_password_hash, check_password_hash)
import datetime


db = SQLAlchemy()


class Rol(db.Model):
    __tablename__ = "rol"
    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(20), unique=True)
    status = db.Column(SmallInteger, nullable=True, default=1)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(255))
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'))
    status = db.Column(SmallInteger, nullable=True, default=1)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

    rol = db.relationship('Rol', backref=db.backref('users', lazy=True))

    def __init__(self, username, password, email):
        self.username = username
        self.password = self.__create_password(password)
        self.email = email

    def __create_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


class Registers(db.Model):
    __tablename__ = 'registers'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255), nullable=False)
    type_id = db.Column(SmallInteger, nullable=False)
    num_id = db.Column(BigInteger, unique=True, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=False)
    phone = db.Column(BigInteger, nullable=False)
    media_id = db.Column(SmallInteger, nullable=True)
    status = db.Column(SmallInteger, default=1, nullable=False)
    create_date = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)


class Types_id(db.Model):
    __tablename__ = 'types_id'
    type_id = db.Column(db.SmallInteger, nullable=False,
                        unique=True, primary_key=True)
    name_id = db.Column(db.String(100), nullable=False, unique=True)


class Medias(db.Model):
    __tablename__ = 'medias'
    media_id = db.Column(SmallInteger, nullable=False, primary_key=True)
    media_name = db.Column(db.String(100), nullable=False, primary_key=True)


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    comment = db.Column(db.Text())
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, comment):
        self.username = username
        self.comment = comment


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    message_send = db.Column(db.Text())
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
