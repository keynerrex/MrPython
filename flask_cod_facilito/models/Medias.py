from . import db
from sqlalchemy import SmallInteger


class Medias(db.Model):
    __tablename__ = 'medias'
    media_id = db.Column(SmallInteger, nullable=False, primary_key=True)
    media_name = db.Column(db.String(100), nullable=False, primary_key=True)
