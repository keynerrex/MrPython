# routes/users.py
from sqlalchemy.exc import IntegrityError, OperationalError
from flask import Blueprint, render_template, request, jsonify, session
from utils.decorators.decorators import admin_role_required, role_required, get_user_by_username, get_session_username
from models import db, User, Rol, Comment

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
        all_users.append({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "create_date": user.create_date.strftime("%d de %B del %Y"),
            "status": user.status if user.status else 'Error de estado',
            "rol": user.rol if user.rol else 'Eror de rol'
        })

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

    return jsonify({
        'userID': user.id,
        "username": user.username,
        "email": user.email,
        "rol_id": int(user.rol_id),
        "status": user.status,
        "create_date": user.create_date.strftime('%d de %B del %Y'),
        "rols": [{"id": rol.id, "rol": rol.rol} for rol in rols]
    })


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
