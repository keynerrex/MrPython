# routes/users.py
from flask import Blueprint, render_template, request, jsonify
from utils.decorators.decorators import admin_role_required
from models.general import User

users_routes = Blueprint('users', __name__)


@users_routes.route('/usuarios_registrados_json', methods=['GET'])
@admin_role_required
def users_registers():
    page = request.args.get('page', 1, type=int)

    users = User.query.with_entities(
        User.username, User.email, User.status, User.create_date
    ).paginate(page=page, per_page=5, error_out=False)

    users_registers = []
    for user in users:
        users_registers.append({
            "username": user.username,
            "email": user.email,
            "status": user.status,
            "create_date": user.create_date.strftime(
                "%d de %B del %Y")
        })

    return jsonify({
        "users_registers": users_registers,
        "total_pages": users.pages
    })


@users_routes.route('/usuarios-registrados', methods=['GET'])
@admin_role_required
def show_users_registers():

    return render_template('users-registers.html',
                           title="Usuarios registrados")
