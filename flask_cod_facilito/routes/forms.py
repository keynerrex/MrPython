import threading
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, render_template, request, current_app, url_for, redirect, flash, jsonify
from utils.decorators import already_logged_in
from models import db, User
from config.mail import mail, Message, MailConfig


forms_routes = Blueprint('forms', __name__)
path_url = '/accesos/'


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


@forms_routes.route(f'{path_url}formulario-ingreso', methods=['GET', 'POST'])
@already_logged_in
def form_to_database():
    if request.method == 'POST':
        try:
            data = request.json
            print(data)
            if not data or 'username' not in data or 'email' not in data or 'password' not in data:
                return jsonify({'error': 'Datos faltantes'}), 400

            username = data['username'].strip().lower()
            email = data['email'].strip().lower()
            password = data['password']

            if not username:
                return jsonify({'error': 'El campo usuario no puede estar vacío'}), 400
            if '@' not in email:
                return jsonify({'error': 'El correo electrónico no es válido'}), 400

            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()

            # Configuración del mensaje de correo
            message = Message(
                'Se ha confirmado el registro en Flask',
                sender=MailConfig.MAIL_USERNAME,
                recipients=[user.email],
                cc='keyneroliveros26@gmail.com'
            )

            message.html = render_template('email.html')

            # Intentar adjuntar imagen al correo
            try:
                with current_app.open_resource("static/img/python_log.jpg") as fp:
                    message.attach(
                        "python_log.jpg", "image/jpeg", fp.read(),
                        'inline', headers=[('Content-ID', '<python_logo>')]
                    )

            except FileNotFoundError:
                print(
                    "Advertencia: Imagen 'python_log.jpg' no encontrada. Se enviará el correo sin imagen.")

            # Enviar el correo en segundo plano con un hilo
            threading.Thread(target=send_async_email, args=(
                current_app._get_current_object(), message)).start()

            return jsonify({'success': True, 'message': 'Usuario registrado correctamente'})

        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'El usuario o el correo electrónico ya están en uso.'}), 400

        except Exception as e:
            db.session.rollback()
            return jsonify({'error': f'Error durante el registro: {str(e)}'}), 500

    return render_template('formulario-ingreso.html'), 200
