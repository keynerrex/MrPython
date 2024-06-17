from flask import (flash, render_template, request,
                   redirect, url_for, Blueprint, session, jsonify)
from models import db, User
from werkzeug.security import generate_password_hash
from utils.decorators.decorators import admin_role_required, login_required, role_required
from sqlalchemy.exc import DataError

passwords_routes = Blueprint('passwords', __name__)
path_url = '/contraseña/'


@passwords_routes.route(f'{path_url}restablecer-contraseña', methods=['GET', 'POST'])
@role_required('Administrador')
def reset_password():
    if request.method == 'POST':
        try:
            data = request.json
            pass_reset = generate_password_hash('123456')
            user = User.query.filter_by(username=data['username']).first()
            if user:
                user.password = pass_reset
                db.session.commit()
                return jsonify({'success': 'Se ha restablecido la clave'}), 200
            else:
                return jsonify({'error': 'Se ha producido un error, Usuario no encontrado'}), 400

        except DataError:
            return jsonify({'error': 'El valor es demasiado grande para realizar la operación, comuniquese con soporte'}), 400
        except Exception as e:
            return jsonify({'error': f'Se ha producido un error {e}'}), 400

    return render_template('reset_password.html'), 200


@passwords_routes.route(f'{path_url}cambiar-contraseña', methods=['GET', 'POST'])
@login_required
def change_password():
    title = 'Cambiar contraseña'

    if request.method == 'POST':
        username = session.get('username')
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        verify_password = request.form.get('verify_password')

        user = User.query.filter_by(username=username).first()

        if user.verify_password(current_password):
            if verify_password == new_password:
                user.password = generate_password_hash(new_password)
                db.session.commit()
                flash('Contraseña cambiada exitosamente')
            else:
                flash('Las contraseñas no coinciden')
        else:
            flash('La contraseña actual no es válida')

    return render_template('change_password.html', title=title)
