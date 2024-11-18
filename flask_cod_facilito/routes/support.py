from flask import (Blueprint, render_template,
                   request, redirect, url_for, flash, jsonify)
from config.config import ProductionConfig
from utils.decorators import role_required
from utils.db_utils import get_data_table
from werkzeug.utils import secure_filename
from models import db, Support, User
import os
from sqlalchemy.exc import IntegrityError, DataError

support_routes = Blueprint('support', __name__)
path_url = '/soporte/'


@support_routes.route(f'{path_url}enviar-soporte', methods=['GET', 'POST'])
def support_ticket():
    if request.method == 'POST':
        username = request.form.get('username')
        details_error = request.form.get('details_error')
        email = request.form.get('email')
        image_path = None


        if 'image_error' in request.files:
            image_file = request.files['image_error']
            if image_file.filename != '':
                upload_folder = ProductionConfig.UPLOAD_FOLDER
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)
                image_path = os.path.join(
                    upload_folder, secure_filename(image_file.filename))
                image_file.save(image_path)

        if details_error and email:
            if image_path is None or username is None:
                image_path,username = 'No se adjunto imagen','Sin usuario'
            try:
                support = Support(
                    username=username, details_error=details_error, image_path=image_path, email=email)
                db.session.add(support)
                db.session.commit()
                return jsonify({'status': 'success', 'message': '¡Ticket de soporte creado exitosamente!'}), 200
            except IntegrityError:
                return jsonify({'status': 'error', 'message': 'Error con la base de datos.'}), 500
            except TypeError:
                return jsonify({'status': 'error', 'message': 'Error procesando el formulario.'}), 500
            except DataError:
                return jsonify({'status': 'error', 'message': 'Error en los datos, verifique nuevamente'}), 500
            finally:
                db.session.rollback()
                db.session.close()
        else:
            return jsonify({'status': 'error', 'message': 'Por favor rellene los campos necesarios'}), 400
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
            "username": ticket.username if ticket.username else 'No se agrego usuario',
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
    ticket = get_data_table(Support, 'support', ticket_id)
    managers = User.query.with_entities(
        User.id,
        User.username
    ).filter(User.rol_id == 4).all()

    if ticket:
        ticket_dict = {
            "ticketID": ticket.id,
            "username": ticket.username if ticket.username else 'No se agrego usuario',
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

        if ticket.ticket_manager_id == 0:
            raise ValueError("ticket_manager_id no puede ser 0")
        if ticket.status not in [0, 1]:
            raise ValueError("El estado debe ser Activo o Inactivo")
        db.session.commit()
        return jsonify({'message': 'El tiquete ha sido actualizado'}), 200
    except Exception as e:
        return jsonify({'message': f'Ha ocurrido un error: {e}'}), 500
