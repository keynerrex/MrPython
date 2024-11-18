from sqlalchemy.exc import IntegrityError
from flask import render_template, request, flash
from flask import Blueprint, render_template, request, current_app, url_for, redirect, flash, jsonify
from utils.decorators import already_logged_in
from models import (db, User, Types_id, Medias, Registers)
from config.mail import mail, Message, MailConfig


forms_routes = Blueprint('forms', __name__)
path_url = '/accesos/'


@forms_routes.route(f'{path_url}formulario-ingreso', methods=['GET', 'POST'])
@already_logged_in
def form_to_database():
    title = "Formulario de ingreso"

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password', username)
        email = request.form.get('email', 'sincorreo@gmail.com')

        if not username:
            return jsonify({'error': 'Error, el usuario no puede estar vacío'}), 400

        user = User(username, password, email)
        message = Message(
            'Se ha confirmado el registro en Flask',
            sender=MailConfig.MAIL_USERNAME,
            recipients=[user.email]
        )
        message.html = render_template('email.html')

        # Adjunta la imagen al correo electrónico
        with current_app.open_resource("static/img/python_log.jpg") as fp:
            message.attach(
                "python_log.jpg", "image/jpeg", fp.read(),
                'inline', headers=[('Content-ID', 'python_logo')]
            )

        try:
            db.session.add(user)
            db.session.commit()
            mail.send(message)
            response = render_template(
                'response_databases.html',
                title="Usuario registrado",
                username=user.username,
                email=user.email
            )
            return jsonify({'success': True, 'html': response})

        except IntegrityError as e:
            # Si hay una violación de la integridad, es probable que sea debido a un usuario o correo electrónico duplicado.
            return jsonify({'error': 'El usuario o el correo electrónico ya están en uso.'}), 400

        except Exception as e:
            return jsonify({'error': f'Error general durante el registro, referencia: {str(e)}'}), 500

    return render_template('formulario-ingreso.html', title=title), 200



