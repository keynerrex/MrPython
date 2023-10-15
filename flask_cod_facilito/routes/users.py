# routes/users.py
from flask import Blueprint, render_template, request
from utils.decorators import admin_role_required
from models.general import User

users_routes = Blueprint('users', __name__)


@users_routes.route('/usuarios-registrados', methods=['GET'])
@admin_role_required
def users_registers():
    title = 'Usuarios registrados'
    users_per_page = 5
    page = request.args.get('page', 1, type=int)

    users = User.query.with_entities(User.username,
                                     User.email,
                                     User.status,
                                     User.create_date).paginate(
        page=page, per_page=users_per_page)
    total_pages = users.pages

    formated_users_registers = []
    for user in users.items:
        formatted_users_registers = user.create_date.strftime(
            "%A %d De %B Del %Y")

        formated_users_registers.append(formatted_users_registers.encode(
            'latin-1').decode('utf-8').capitalize())

    return render_template('users-registers.html',
                           title=title,
                           users=users,
                           formated_users_registers=formated_users_registers,
                           total_pages=total_pages)
