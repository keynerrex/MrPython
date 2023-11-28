from . import db
from sqlalchemy import SmallInteger
import datetime


class Comment(db.Model):
    """Modelo de tabla BD para los comentarios hechos por usuarios"""
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    comment = db.Column(db.Text)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    status = db.Column(SmallInteger, nullable=False, default=1)

    def __init__(self, username, comment):
        self.username = username
        self.comment = comment

    def __str__(self) -> str:
        return super().__str__()
