from config.mail import Config


class DevelopmentConfig(Config):

    DEBUG = True
    DB_NAME = 'flask'
    DB_USER = 'keynerrex'
    DB_SERVER = 'localhost'
    DB_PASS = 'keynerdel2015'
    DB_PORT = 3307
    SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USER}:{DB_PASS}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = True
    DB_NAME = 'flask'
    DB_USER = 'root'
    DB_SERVER = '127.0.0.1'
    DB_PASS = '12345678'
    DB_PORT = 3307
    SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USER}:{DB_PASS}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
