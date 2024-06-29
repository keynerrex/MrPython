from flask import (flash, render_template, request,
                   Blueprint, session, jsonify)
from models import db, User
from werkzeug.security import generate_password_hash
from utils.decorators import login_required, role_required
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
    if request.method == 'POST':
        try:
            data = request.json
            username = session.get('username')
            user = User.query.filter_by(username=username).first()

            if user:
                current_password = data['current_password']
                new_password = data['new_password']
                verify_password = data['verify_password']

                # Validar que las contraseñas no estén vacías
                if not current_password or not new_password or not verify_password:
                    return jsonify({'error': 'Las contraseñas no pueden estar vacías'}), 400

                # Validar que las contraseñas tengan al menos 5 dígitos
                if len(current_password) < 5 or len(new_password) < 5 or len(verify_password) < 5:
                    return jsonify({'error': 'Las contraseñas deben tener al menos 5 dígitos'}), 400

                if not user.verify_password(current_password):
                    return jsonify({'error': 'La contraseña actual no es válida'}), 400
                if new_password != verify_password:
                    return jsonify({'error': 'Las contraseñas no coinciden'}), 400

                user.password = generate_password_hash(new_password)
                db.session.commit()
                return jsonify({'success': 'Contraseña actualizada'})
            else:
                return jsonify({'error': 'Usuario no encontrado'}), 404

        except Exception as e:
            print(e)
            return jsonify({'error': 'Ha ocurrido un error al cambiar la contraseña'}), 500
    return render_template('change_password_.html'), 200
