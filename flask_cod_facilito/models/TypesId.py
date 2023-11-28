from . import db
from sqlalchemy import SmallInteger


class Types_id(db.Model):
    __tablename__ = 'types_id'
    type_id = db.Column(db.SmallInteger, nullable=False,
                        unique=True, primary_key=True)
    name_id = db.Column(db.String(100), nullable=False, unique=True)
