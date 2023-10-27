from flask import (Blueprint, redirect, session, url_for,
                   render_template, request, jsonify)
from models.general import db, Rol
from utils.decorators.decorators import admin_role_required
from forms.web_form import AddRolForm

roles_routes = Blueprint('roles', __name__)


@roles_routes.route('/crear-rol', methods=['GET', 'POST'])
@admin_role_required
def add_rol():
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
@admin_role_required
def response_rol():
    rol = request.args.get(
        'rol', 'No se ha encontrado ningún rol').capitalize()
    return render_template('response_rol.html',
                           title="Datos Recibidos",
                           rol=rol)


@roles_routes.route('/roles_json', methods=['GET'])
@admin_role_required
def role_json():
    page = request.args.get('page', 1, type=int)

    rols = Rol.query.with_entities(
        Rol.rol, Rol.status, Rol.create_date
    ).paginate(page=page, per_page=5, error_out=False)

    rols_created = []
    for rol in rols:
        rols_created.append({
            "rol": rol.rol,
            "status": rol.status,
            "create_date": rol.create_date.strftime(
                "%d de %B del %Y"
            )
        })

    return jsonify({
        "rols_created": rols_created,
        "total_pages": rols.pages
    })


@roles_routes.route('/roles-creados', methods=['GET'])
@admin_role_required
def show_roles():
    return render_template('roles.html',
                           title='Roles creados')