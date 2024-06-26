from flask import (Blueprint, redirect, url_for,
                   render_template, request, jsonify)
from models import db, Rol
from utils.decorators import role_required
from forms.web_form import AddRolForm

roles_routes = Blueprint('roles', __name__)
path_url = '/roles/'


@roles_routes.route(f'{path_url}crear-rol', methods=['GET', 'POST'])
@role_required('Administrador')
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


@roles_routes.route(f'{path_url}response_rol', methods=['GET'])
@role_required('Administrador')
def response_rol():
    rol = request.args.get(
        'rol', 'No se ha encontrado ningún rol').capitalize()
    return render_template('response_rol.html',
                           title="Datos Recibidos",
                           rol=rol)


@roles_routes.route(f'{path_url}roles_json', methods=['GET'])
@role_required('Administrador')
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


@roles_routes.route(f'{path_url}roles-creados', methods=['GET'])
@role_required('Administrador')
def show_roles():
    return render_template('roles.html',
                           title='Roles creados')


@roles_routes.route(f'{path_url}eliminar_rol', methods=['GET', 'POST'])
@role_required('Administrador')
def eliminar_rol():

    rolName = request.form.get('rolName', 'No se encontró ningun rol')
    try:
        rol = Rol.query.filter_by(rol=rolName).first()

        if rol:
            db.session.delete(rol)
            db.session.commit()
            return jsonify({'title': 'Acción completada',
                            'mensaje': 'Rol eliminado correctamente',
                            'icon': 'success'})
        else:
            return jsonify({'title': 'Ha ocurrido un error',
                            'mensaje': 'No se pudo encontrar el rol',
                            'icon': 'error'})
    except Exception as e:
        return jsonify({'title': 'Ha ocurrido un error, por favor comuniquese con soporte',
                        'mensaje': f'{e}',
                        'icon': 'warning'})
