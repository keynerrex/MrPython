from configs.mail import Config


class DevelopmentConfig(Config):

    DEBUG = True
    DB_NAME = 'flask'
    DB_USER = 'keynerrex'
    DB_SERVER = 'localhost'
    DB_PASS = 'keynerdel2015'
    DB_PORT = 3307
    SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USER}:{DB_PASS}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
