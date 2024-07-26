# routes/users.py
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, render_template, request, jsonify, session
from utils.decorators import admin_role_required
from models import db, User, Rol

users_routes = Blueprint('users', __name__)

path_url = '/usuarios/'


@users_routes.route(f'{path_url}usuarios')
@admin_role_required
def usuarios():
    return render_template('usuarios.html')


@users_routes.route(f'{path_url}usuarios_json')
@admin_role_required
def usuarios_json():
    users = User.query.with_entities(
        User.id,
        User.username,
        User.email,
        User.status,
        User.create_date,
        Rol.rol
    ).outerjoin(Rol).all()
    all_users = []
    for user in users:
        users_list = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "status": user.status,
            "rol": user.rol if user.rol else 'Eror de rol'
        }
        if user.create_date:
            users_list['create_date'] = user.create_date.strftime(
                "%d de %B del %Y")
        else:
            users_list['create_date'] = 'Sin fecha'
        all_users.append(users_list)

    return jsonify({
        "ResponseCode": "200 OK",
        "CodeResponse": 200,
        "all_users": all_users
    }), 200


@users_routes.route(f'{path_url}usuarios/<int:userId>', methods=['GET'])
def get_user_data(userId):
    user = User.query.get(userId)
    rols = User.query.with_entities(
        Rol.id,
        Rol.rol
    ).all()
    user_data = {
        'userID': user.id,
        "username": user.username,
        "email": user.email,
        "rol_id": int(user.rol_id),
        "status": user.status,
        "rols": [{"id": rol.id, "rol": rol.rol} for rol in rols]
    }
    if user.create_date:
        user_data['create_date'] = user.create_date.strftime('%d de %B del %Y')
    else:
        user_data['create_date'] = 'Sin fecha'
    return jsonify(user_data)


@users_routes.route(f'{path_url}usuarios/<int:userId>', methods=['POST'])
def update_user_data(userId):
    user = User.query.get(userId)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    try:
        data = request.json
        if 'username' in data:
            user.username = data['username']
            if user.username == '':
                raise ValueError('El campo no puede estar vacío')
        if 'email' in data:
            user.email = data['email']
            if '@' not in user.email:
                raise ValueError('Campos faltantes')
            if 'rol_id' in data:
                user.rol_id = data['rol_id']
        if 'status' in data:
            user.status = data['status']
        if user.status not in [0, 1]:
            raise ValueError("El estado debe ser Activo o Inactivo")
        db.session.commit()
        return jsonify({'message': 'El usuario ha sido actualizado'}), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': f'Error de integridad en la base de datos, verifique que no halla datos existentes repetidos'}), 500
    except Exception as e:
        return jsonify({'message': f'Ha ocurrido un error: {e}'}), 500
