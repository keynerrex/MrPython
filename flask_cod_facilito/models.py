from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

# Modelos
db = SQLAlchemy()


# Modelo user
class User(db.Model):
    # Atributos = Columnas base datos
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(255))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, password, email):
        self.username = username
        self.password = self.__create_password(password)
        self.email = email

    def __create_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


# if __name__ == '__main__':

#     passw = '12345678@'
#     user1 = User('keynerrex', passw, 'keyneroliveros24@gmail.com')
#     print(user1.password)
#     print(user1.verify_password(passw))
    
#     bkdf2:sha256:260000$8xHZYf15nX2KGRdj$c78833a098f2add60e607ed09b5a