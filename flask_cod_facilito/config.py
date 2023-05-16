# Leerlo de nuestra variable de entorno
import os


# Configuraciones por entorno
class Config(object):
    # Llave secreta
    SECRET_KEY = "mi_llave"


# Configuracion para desarrollo
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://keynerrex:keynerdel2015@localhost:3307/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
