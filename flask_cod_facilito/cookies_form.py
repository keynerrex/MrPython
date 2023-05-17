from wtforms import Form, StringField, EmailField, validators, HiddenField
from wtforms import PasswordField
from models import User

# Este es la funcion para validar el campo del CSRF


def campo_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacío')


# Esta es la clase donde se lleva la ruta del comentario_to_formulario()
class ComentarForm(Form):
    # Crea los inputs del html y sus validaciones
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

    password = PasswordField('Password',
                             [
                                 validators.DataRequired(
                                     message="El password es requerido"),
                                 validators.length(
                                     min=4, max=25, message="Ingrese una password valida!.")
                             ])


class CreateForm(Form):
    # Crea los inputs del html y sus validaciones
    username = StringField('Usuario', [
        validators.DataRequired(message="El usuario es requerido"),
        validators.Length(min=4, max=50, message="Ingrese un nombre valido!."),
    ])
    email = EmailField('Correo', [
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingrese un correo valido"),
        validators.length(min=4, max=50, message="Ingrese un email valido")
    ])
    password = PasswordField('Contraseña', [
        validators.DataRequired(message="La contraseña es requerida"),
        validators.length(
            min=4, max=50, message="Ingrese una contraseña valida")
    ])

    # def validate_username(form, field):
    #     username = field.data
    #     user = User.query.filter_by(username=username).first()
    #     if user is not None:
    #         raise validators.ValidationError(
    #             "El usuario ya se encuentra registrado")
