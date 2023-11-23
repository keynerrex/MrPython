import os
from flask_mail import Mail, Message
mail = Mail()


class MailConfig(object):
    """
    Configuración del correo electronico para enviar emails

    Atributos:
    SECRET_KEY: Llave secreta para la configuración CSRD
    MAIL_SERVER: Configuración del servidor email
    MAIL_PORT: Puerto de conexión del email
    MAIL_USE_TLS: Ni idea
    MAIL_USERNAME: Correo electronico para el envio de emails
    MAIL_PASSWORD: Contraseña del correo electronico
    """
    SECRET_KEY = os.getenv('SECRET_KEY')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
