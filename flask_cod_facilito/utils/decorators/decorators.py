from models import User
from flask import session, redirect, url_for, render_template
from functools import wraps
# Asegúrate de importar tus modelos adecuadamente
from models import db, User, Rol


def admin_role_required(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('home.login'))

        username = session.get('username')
        user = User.query.filter_by(username=username).first()

        if not user or user.status != 1:
            return render_template('inauthorized.html', code_err=401), 401

        # Verificar si el usuario tiene el rol de Administrador
        if user.rol.rol != 'Administrador':
            return render_template('inauthorized.html', code_err=401), 401

        return view(*args, **kwargs)

    return decorated_view


def role_required(*allowed_roles):
    def decorator(view):
        @wraps(view)
        def decorated_view(*args, **kwargs):
            if 'username' not in session:
                return redirect(url_for('home.login'))

            username = session.get('username')
            user = User.query.filter_by(username=username).first()

            if not user or user.status != 1 or not user.rol:
                return render_template('inauthorized.html', code_err=401), 401

            # Permitir el acceso si no se proporcionan roles específicos o si el usuario tiene uno de los roles permitidos
            if not allowed_roles or user.rol.rol in allowed_roles:
                return view(*args, **kwargs)

            return render_template('inauthorized.html', code_err=401), 401

        return decorated_view

    return decorator


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

        username = session.get('username')
        user = User.query.filter_by(username=username).first()
        print(user)
        if user.status != 1:
            return render_template('user_inactive.html'), 403
        return view(*args, **kwargs)
    return decorated_view


def already_logged_in(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        if 'username' in session:
            return redirect(url_for('home.index'))

        return view(*args, **kwargs)
    return decorated_view
