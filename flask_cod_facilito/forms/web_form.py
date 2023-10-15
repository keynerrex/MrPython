from wtforms import Form, StringField, EmailField, validators, HiddenField
from wtforms import PasswordField
from models.general import User, Rol


# Este es la funcion para validar el campo del CSRF
def campo_honeypot(form, field):
    if field.data and len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacío')


# Esta es la clase donde se lleva la ruta del comment_to_form()
class ComentarForm(Form):
    comment = StringField('Comentario')
    honeypot = HiddenField('', [campo_honeypot])


class LoginForm(Form):
    username = StringField('Usuario',
                           [
                               validators.DataRequired(
                                   message="El username es requerido"),
                               validators.length(
                                   min=4, max=25, message="Ingrese un usuario valido!.")
                           ])

    password = PasswordField('Contraseña',
                             [
                                 validators.DataRequired(
                                     message="El password es requerido"),
                                 validators.length(
                                     min=4, max=25, message="Ingrese una password valida!.")
                             ])


class AddRolForm(Form):
    rol = StringField('Rol', [
        validators.DataRequired(message="Debe agregar un rol"),
        validators.Regexp(
            '^[a-zA-Z]+$',
            message="El rol debe contener solo letras, sin espacios ni caracteres especiales")
    ])
    honeypot = HiddenField('', [campo_honeypot])

    def validate_rol(form, field):
        rol_ = field.data
        rol = Rol.query.filter_by(rol=rol_).first()
        if rol:
            raise validators.ValidationError(
                "Ya este rol existe")


class CreateForm(Form):
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

    def validate_username(form, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user:
            raise validators.ValidationError(
                "El usuario ya se encuentra registrado")

    def validate_email(form, field):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if user:
            raise validators.ValidationError(
                "Este correo ya se encuentra registrado")
