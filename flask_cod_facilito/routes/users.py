# routes/users.py
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, render_template, request, jsonify
from utils.decorators.decorators import admin_role_required
from models import db, User, Rol

users_routes = Blueprint('users', __name__)

path_url = '/usuarios/'


@users_routes.route(f'{path_url}usuarios')
def usuarios():
    return render_template('usuarios.html')


@users_routes.route(f'{path_url}usuarios_json')
def usuarios_json():
    users = User.query.with_entities(
        User.id,
        User.username,
        User.email,
        User.status,
        User.create_date,
        User.rol_id
    ).all()
    all_users = []
    for user in users:
        all_users.append({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "create_date": user.create_date.strftime("%d de %B del %Y"),
            "status": user.status,
            "rol": user.rol_id
        })

    return jsonify({
        "ResponseCode": "200 OK",
        "CodeResponse": 200,
        "all_users": all_users
    }), 200


@users_routes.route(f'{path_url}prueba')
def prueba():
    return render_template('prueba.html')


@users_routes.route(f'{path_url}registros')
def registros():
    return render_template('registros.html')


@users_routes.route(f'{path_url}usuarios_registrados_json', methods=['GET'])
@admin_role_required
def users_registers():
    page = request.args.get('page', 1, type=int)
    search_term = request.args.get('search', '', type=str)
    # Query para traer los datos y filtra por busdcador si es necesario
    users = User.query.with_entities(
        User.id,
        User.username,
        User.email,
        User.status,
        User.create_date,
        Rol.rol
    ).join(Rol).filter(
        User.username.ilike(
            f"%{search_term}%")).paginate(
        page=page, per_page=5, error_out=False)

    users_registers = []
    for user in users:
        users_registers.append({
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "status": user.status,
            "rol": user.rol,
            "create_date": user.create_date.strftime("%d de %B del %Y")
        })

    return jsonify({
        "users_registers": users_registers,
        "total_pages": users.pages
    })


@users_routes.route(f'{path_url}usuarios-registrados', methods=['GET'])
@admin_role_required
def show_users_registers():
    rols = Rol.query.order_by(Rol.rol).all()

    return render_template('users-registers.html',
                           title="Usuarios registrados",
                           rols=rols)


@users_routes.route(f'{path_url}editar-usuario', methods=['POST'])
def edit_user():
    try:
        # Obtener datos del formulario
        id = request.form.get('user_id')
        username = request.form.get('username')
        email = request.form.get('email')
        rol = int(request.form.get('rol'))
        status = int(request.form.get('status'))

        # Validaciones
        if len(username) < 3:
            return jsonify({'error': 'El nombre de usuario debe tener al menos 3 caracteres'}), 400

        if username.isdigit():
            return jsonify({'error': 'El nombre de usuario no puede consistir solo en números'}), 400

        if username.isspace() or ' ' in username:
            return jsonify({'error': 'El nombre de usuario no puede contener espacios en blanco'}), 400

        # Verificar si el nombre de usuario ya existe para otros usuarios
        existing_user = User.query.filter(
            User.id != id, User.username == username).first()
        existing_email = User.query.filter(
            User.id != id, User.email == email).first()

        if existing_user:
            return jsonify({'error': 'El nombre de usuario ya está en uso'}), 400
        elif existing_email:
            return jsonify({'error': 'Este correo ya está en uso'}), 400

        # Actualizar la información del usuario en la base de datos
        user = User.query.filter_by(id=id).first()
        if user:
            user.username = username
            user.email = email
            user.rol_id = rol
            user.status = status
            db.session.commit()
            return jsonify({'message': 'Usuario actualizado correctamente'}), 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404

    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Error de integridad en la base de datos'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
