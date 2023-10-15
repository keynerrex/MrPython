from flask_mail import Mail, Message
mail = Mail()


class Config(object):
    SECRET_KEY = "kef8wd68$$@3#fdg__7gtdf"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'australiayt35@gmail.com'
    PASS_SECRET = 'bxzpdqroqzqgvwkt'
