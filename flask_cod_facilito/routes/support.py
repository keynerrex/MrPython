from flask import (Blueprint, render_template,
                   request, redirect, url_for, flash, jsonify)
from config.config import ProductionConfig
from utils.decorators.decorators import role_required
from werkzeug.utils import secure_filename
from models import db, Support, User
import os
from sqlalchemy.exc import IntegrityError
support_routes = Blueprint('support', __name__)
path_url = '/soporte/'


@support_routes.route(f'{path_url}enviar-soporte', methods=['GET', 'POST'])
def support_ticket():
    """Función para crear un ticket de soporte"""

    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form.get('username', 'Sin usuario')
        details_error = request.form.get('details_error')
        email = request.form.get('email', 'No se ha adjuntado un correo')
        image_path = None

        if not email:
            flash('Error: El correo es obligatorio', 'error',)
        elif not details_error:
            flash('Error: Es necesario llenar el detalle', 'error')

        # Verificar si se ha subido una imagen
        if 'image_error' in request.files:
            image_file = request.files['image_error']

            if image_file.filename != '':
                upload_folder = ProductionConfig.UPLOAD_FOLDER

                # Asegúrate de que el directorio de carga exista
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)

                # Guardar la imagen y obtener la ruta
                image_path = os.path.join(
                    upload_folder, secure_filename(image_file.filename))
                image_file.save(image_path)

        if details_error and email:
            if image_path is None:
                image_path = 'No se adjunto ninguna imagen'
            try:
                support = Support(
                    username=username, details_error=details_error, image_path=image_path, email=email)
                # Agregar la instancia a la sesión y guardar en la base de datos
                db.session.add(support)
                db.session.commit()

                # Redireccionar a una nueva página después del envío exitoso
                flash('¡Ticket de soporte creado exitosamente!', 'success')
                return redirect(url_for('support.support_ticket'))

            except IntegrityError as ie:
                flash('Error: Se produjo un problema con la base de datos.', 'error')

            except TypeError as e:
                flash(
                    'Error: Se produjo un problema durante el procesamiento del formulario.', 'error')

            finally:
                db.session.rollback()
                db.session.close()

    return render_template('support_ticket.html', title='Soporte'), 200


@support_routes.route(f'{path_url}tickets-soporte')
@role_required('Soporte', 'Administrador')
def assign_support():

    return render_template('assign_support.html'), 200


@support_routes.route(f'{path_url}tickets_json')
@role_required('Soporte', 'Administrador')
def tickets_json():
    supports = Support.query.with_entities(
        Support.id,
        Support.username,
        Support.details_error,
        Support.image_path,
        Support.email,
        User.username.label('ticket_manager_username'),
        Support.status,
        Support.create_date,
    ).outerjoin(User).all()
    tickets = []
    for ticket in supports:
        tickets_dict = {
            "id": ticket.id,
            "username": ticket.username,
            "details_error": ticket.details_error,
            "image_path": ticket.image_path,
            "email": ticket.email,
            "ticket_manager_username": ticket.ticket_manager_username,
            "status": ticket.status,
        }
        # Verificar si hay fecha correcta, en caso no haya o sea null, se devolverá sin fecha
        if ticket.create_date:
            tickets_dict['create_date'] = ticket.create_date.strftime(
                '%d de %B del %Y')
        else:
            tickets_dict['create_date'] = 'Sin fecha'
        tickets.append(tickets_dict)
    return jsonify({
        "ResponseCode": "200 OK",
        "CodeResponse": 200,
        "tickets": tickets
    }), 200


@support_routes.route(f'{path_url}ticket/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    ticket = Support.query.get(ticket_id)
    managers = User.query.with_entities(
        User.id,
        User.username
    ).filter(User.rol_id == 4).all()

    if ticket:
        ticket_dict = {
            "ticketID": ticket.id,
            "username": ticket.username,
            "details_error": ticket.details_error,
            "email": ticket.email,
            "ticket_manager_username": ticket.ticket_manager_id,
            "status": ticket.status,
            "managers": [{"id": manager.id, "username": manager.username} for manager in managers]
        }

        # Verificar si hay fecha correcta, en caso no haya o sea null, se devolverá sin fecha
        if ticket.create_date:
            ticket_dict["create_date"] = ticket.create_date.strftime(
                '%d de %B del %Y')
        else:
            ticket_dict["create_date"] = "Sin fecha"

        return jsonify(ticket_dict)
    else:
        return jsonify({'error': 'Ticket not found'}), 404


@support_routes.route(f'{path_url}ticket/<int:ticket_id>', methods=['POST'])
def update_ticket(ticket_id):
    ticket = Support.query.get(ticket_id)
    if not ticket:
        return jsonify({'error': 'Ticket not found'}), 404
    try:
        data = request.json

        if 'ticket_manager_id' in data:
            ticket.ticket_manager_id = data['ticket_manager_id']
        if 'status' in data:
            ticket.status = data['status']

        if ticket.ticket_manager_id == 0:  # Por ejemplo, si el ticket_manager_id es 0
            raise ValueError("ticket_manager_id no puede ser 0")
        if ticket.status not in [0, 1]:
            raise ValueError("El estado debe ser Activo o Inactivo")
        db.session.commit()
        return jsonify({'message': 'El tiquete ha sido actualizado'}), 200
    except Exception as e:
        return jsonify({'message': f'Ha ocurrido un error: {e}'}), 500
