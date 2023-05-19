# Leerlo de nuestra variable de entorno
import os

# Configuraciones por entorno


class Config(object):
    # Llave secreta
    SECRET_KEY = "mi_llave"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PROT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'australiayt35@gmail.com'
    MAIL_PASSWORD = 'bxzpdqroqzqgvwkt'


# Configuracion para desarrollo
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://keynerrex:keynerdel2015@localhost:3307/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
