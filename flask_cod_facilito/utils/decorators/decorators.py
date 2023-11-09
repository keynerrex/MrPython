from flask import session, redirect, url_for, render_template
from functools import wraps
# Asegúrate de importar tus modelos adecuadamente
from models.general import db, User, Rol


def admin_role_required(adm_user):
    @wraps(adm_user)
    def decorated_rol(*args, **kwargs):
        username = session.get('username')
        rol_administrador = db.session.query(User.username, Rol.rol)\
            .join(Rol).filter(
                User.username == username,
                Rol.rol == 'Administrador').first()

        if not rol_administrador:
            return inauthorized()

        return adm_user(*args, **kwargs)

    return decorated_rol


def inauthorized():
    code_err = 401
    return render_template('inauthorized.html',
                           code_err=code_err), code_err


def function_no_available():
    cod_error = 403
    return render_template('not_available.html',
                           cod_error=cod_error), cod_error


def no_available(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        return function_no_available()
    return decorated_view


def login_required(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('home.login'))
        return view(*args, **kwargs)
    return decorated_view


def already_logged_in(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        if 'username' in session:
            return redirect(url_for('home.index'))
        return view(*args, **kwargs)
    return decorated_view
