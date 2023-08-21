# Leerlo de nuestra variable de entorno
import os


# Configuraciones por entorno
class Config(object):
    SECRET_KEY = "kef8wd68$$@3#fdg__7gtdf"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PROT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'australiayt35@gmail.com'
    PASS_SECRET = 'bxzpdqroqzqgvwkt'
    MAIL_PASSWORD = f'{PASS_SECRET}'


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = 'flask'
    DB_USER = 'keynerrex'
    DB_SERVER = 'localhost'
    DB_PASS = ''
    DB_PORT = 3306
    SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USER}:{DB_PASS}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql://user@production_host/database"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
