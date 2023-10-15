from flask import Blueprint, redirect, session, url_for, render_template, request
from models.general import db, Rol
from utils.decorators.decorators import admin_role_required
from forms.web_form import AddRolForm

roles_routes = Blueprint('roles', __name__)


@roles_routes.route('/crear-rol', methods=['GET', 'POST'])
@admin_role_required
def add_rol():
    if 'username' not in session:
        return redirect(url_for('login'))

    title = 'Crear roles'
    rol_form = AddRolForm(request.form)

    if request.method == 'POST' and rol_form.validate():
        rol_ = Rol(
            rol=rol_form.rol.data.capitalize())

        db.session.add(rol_)
        db.session.commit()
        return redirect(url_for('roles.response_rol',
                                rol=rol_form.rol.data))

    return render_template('add_rol.html',
                           title=title,
                           form=rol_form)


@roles_routes.route('/response_rol', methods=['GET'])
def response_rol():
    rol = request.args.get('rol').capitalize()
    return render_template('response_rol.html',
                           title="Datos Recibidos",
                           rol=rol)


@roles_routes.route('/roles-creados', methods=['GET'])
@admin_role_required
def show_roles():
    title = 'Roles Creados'
    rol_per_page = 5
    page = request.args.get('page', 1, type=int)

    roles = Rol.query.with_entities(Rol.rol,
                                    Rol.create_date,
                                    Rol.status).paginate(
        page=page, per_page=rol_per_page)

    formated_roles = []
    for rol in roles.items:
        formatted_roles = rol.create_date.strftime("%A %d De %B Del %Y")
        formated_roles.append(formatted_roles.encode(
            'latin-1').decode('utf-8').capitalize())

    total_pages = roles.pages
    return render_template('roles.html',
                           title=title,
                           roles=roles,
                           formatted_roles=formated_roles,
                           total_pages=total_pages)
