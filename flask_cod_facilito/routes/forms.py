from flask import Blueprint, render_template, request, current_app, url_for, redirect, flash
from utils.decorators.decorators import already_logged_in
from forms.web_form import CreateForm
from models.general import (db, User, Types_id, Medias, Registers)
from config.mail import mail, Message, MailConfig
from smtplib import SMTPException, SMTPAuthenticationError


forms_routes = Blueprint('forms', __name__)
path_url = '/accesos/'


@forms_routes.route(f'{path_url}formulario-ingreso', methods=['GET', 'POST'])
@already_logged_in
def form_to_database():
    """Función para registrar un usuario al sistema"""
    title = "Formulario de ingreso"
    create_formulario = CreateForm(request.form)

    if request.method == 'POST' and create_formulario.validate():
        user = User(create_formulario.username.data,
                    create_formulario.password.data,
                    create_formulario.email.data)

        try:
            """Se hace la configuración de email para ser enviado al correo destino
            sender: el correo desde donde se enviara
            recipients: los correos o correo al que se va enviar
            """
            message = Message('Te has registrado en Flask',
                              sender=MailConfig.MAIL_USERNAME,
                              recipients=[user.email])

            # Referencia del html ya diseñado que sera enviado por el email
            message.html = render_template('email.html',
                                           user=user.username)
            # Envío del mensaje y renderizado del html exitoso
            mail.send(message)
            response = render_template('response_databases.html',
                                       title="Usuario registrado",
                                       username=user.username,
                                       email=user.email)
            db.session.add(user)
            db.session.commit()
            return response
        except SMTPException as e:
            """Se renderiza el html por si ocurre un erro y mostrandonos la referencia"""
            return render_template('response_general.html',
                                   h3=f'Ha ocurrido un eror, referencia: {e}',
                                   title_swal='Ocurrió un problema',
                                   icon='warning')
        finally:
            # Se regresa el cambio de la db si ocurre algo
            db.session.rollback()
            db.session.close()

    return render_template('formulario-ingreso.html',
                           form=create_formulario,
                           title=title)


@forms_routes.route(f'{path_url}registrarme', methods=['GET', 'POST'])
@already_logged_in
def registers():
    title = 'Registrarme'
    # Obetner los tipos de identificación y las medias sociales
    types = db.session.query(Types_id).order_by(Types_id.type_id.asc()).all()
    medias = db.session.query(Medias).order_by(Medias.media_id.asc()).all()

    # Obtener los valores del envio del formulario html
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        type_id = request.form.get('type_id')
        num_id = request.form.get('num_id')
        email = request.form.get('email')
        phone = request.form.get('phone')
        media_id = request.form.get('media_id')

        if len(fullname) < 5:
            flash('El nombre es muy corto, debe tener al menos 5 caracteres')
        elif "@" not in email:
            flash('El email no es valido')
        elif len(phone) != 10:
            flash('Numero invalido')
        elif len(num_id) < 7 or len(num_id) > 10:
            flash("Numero de identifación invalida")
        else:
            register = Registers(fullname=fullname,
                                 type_id=type_id,
                                 num_id=num_id,
                                 email=email,
                                 phone=phone,
                                 media_id=media_id)

            db.session.add(register)
            db.session.commit()
            return redirect(url_for('responses.response_registers'))

    return render_template('registers.html',
                           title=title,
                           types=types,
                           medias=medias)
