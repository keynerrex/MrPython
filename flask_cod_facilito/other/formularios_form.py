from wtforms import Form, StringField, EmailField, validators, HiddenField
from wtforms import PasswordField


def campo_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacío')


class ComentarForm(Form):
    username = StringField('Usuario', [
        validators.DataRequired(message="El usuario es requerido"),
        validators.length(min=3, max=25, message="Ingrese un nombre valido!.")
    ])
    email = EmailField('Correo', [
        validators.DataRequired(message="El correo es requerido")
    ])
    comment = StringField('Comentario')
    honeypot = HiddenField('', [campo_honeypot])


class LoginForm(Form):
    username = StringField('Username',
                           [
                               validators.DataRequired(
                                   message="El username es requerido"),
                               validators.length(
                                   min=4, max=25, message="Ingrese un usuario valido!.")
                           ])

    password = PasswordField('Password', [
                             validators.DataRequired(
                                 message="El password es requerido"),
                             validators.length(
                                 min=4, max=25, message="Ingrese una password valida!.")])
