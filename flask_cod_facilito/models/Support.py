# Supporet.py (renombrado a Support.py)
from . import db
from sqlalchemy import SmallInteger
import datetime


class Support(db.Model):
    __tablename__ = "support"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    details_error = db.Column(db.Text)
    image_path = db.Column(db.String(255))
    ticket_manager_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('support', lazy=True))
    status = db.Column(SmallInteger, nullable=True, default=1)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, details_error, image_path, status=1):
        self.username = username
        self.details_error = details_error
        self.image_path = image_path
        self.status = status

    def assign_manager(self, ticket_manager_id):
        self.ticket_manager_id = ticket_manager_id
