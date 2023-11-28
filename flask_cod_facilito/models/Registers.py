from . import db
from sqlalchemy import SmallInteger, BigInteger
import datetime


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
