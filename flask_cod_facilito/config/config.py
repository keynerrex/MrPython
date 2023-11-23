from dotenv import load_dotenv
from config.mail import MailConfig
import os

load_dotenv()


class DevelopmentConfig(MailConfig):
    """
    Configuración para ambiente de desarrollo

    Atributos:
    DB_NAME: Nombre de la base de datos
    DB_USER: Obtener el nombre del usuario
    DB_SERVER: Ip donde se encuentra alojada la base de datos
    DB_PASS: Obtener la contraseña de la base de datos
    DB_PORT: Puerto donde se encuentra la base de datos
    SQLALCHEMY_DATABASE_URI: Ni idea
    SQLALCHEMY_TRACK_MODIFICATIONS: Ni idea
    """
    DEBUG = True
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_SERVER = os.getenv('DB_SERVER')
    DB_PASS = os.getenv('DB_PASS')
    DB_PORT = os.getenv('DB_PORT')
    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASS}@{DB_SERVER}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
