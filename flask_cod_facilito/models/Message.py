from . import db
import datetime


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    message_send = db.Column(db.Text)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
