from typing import Optional
from flask import render_template
from config.mail import mail, MailConfig, Message


def get_data_table(model_class: type, table: Optional[str] = None, id: int = None) -> type:
    """
    Obtiene los datos de una tabla específica y un ID dado.

    ## Parámetros
    - `model_class` (SQLAlchemy Model): Clase del modelo de la tabla.
    - `table` (str, opcional): Nombre de la tabla. Si no se proporciona, se utilizará el nombre de la clase del modelo.
    - `id` (int, opcional): ID del registro a buscar. Si no se proporciona, se devolverá toda la información de la tabla.

    ## Retorna
    - `SQLAlchemy Model`: Registro encontrado.
    """
    if table is None:
        table = model_class.__tablename__

    if id is None:
        return model_class.query.all()
    else:
        return model_class.query.get(id)


# Funcion que genera un envio a gmail con el contexto que pongamos
def send_mail(title: str, email_to: str, context: dict, html: str):
    try:
        email = ''.join(email_to)
        message = Message(
            title,
            sender=MailConfig.MAIL_USERNAME,
            recipients=[email]
        )
        message.html = render_template(
            html, **context)
        mail.send(message)
        return True
    except Exception as e:
        return False
