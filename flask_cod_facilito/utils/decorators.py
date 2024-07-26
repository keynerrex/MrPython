from flask import session, redirect, url_for, render_template
from functools import wraps
from models import User
from typing import Optional


# Función que devuelve el usuario que tiene sesión abierta
def get_session_username():
    return session.get('username')


# Función que busca por el username si existe en la base de datos
def get_user_by_username(username: str) -> Optional[User]:
    return User.query.filter_by(username=username).first()


# Decorador para pedir el rol de administrador para el acceso
def admin_role_required(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        username = get_session_username()
        user = get_user_by_username(username)

        if not user or user.status != 1 or user.rol.rol != 'Administrador':
            return render_template('inauthorized.html', code_err=401), 401

        return view(*args, **kwargs)

    return decorated_view


# Decorador para dar accesos a vistas con los roles seleccionados
def role_required(*allowed_roles):
    def decorator(view):
        @wraps(view)
        def decorated_view(*args, **kwargs):
            username = get_session_username()
            user = get_user_by_username(username)

            if not user or user.status != 1 or not user.rol:
                return render_template('inauthorized.html', code_err=401), 401

            if not allowed_roles or user.rol.rol in allowed_roles:
                return view(*args, **kwargs)

            return render_template('inauthorized.html', code_err=401), 401

        return decorated_view

    return decorator


# Función que retorna el html de acceso no autorizado
def inauthorized():
    code_err = 401
    return render_template('inauthorized.html', code_err=code_err), 401


# Función que retorna el html de pagina no disponible
def function_no_available():
    cod_error = 403
    return render_template('not_available.html', cod_error=cod_error), 403


# Función para dar un mensaje en la web que el recurso no se encuentra disponible
def no_available(view):
    @wraps(view)
    def decorated_view():
        return function_no_available()

    return decorated_view


# Función para validar si ha iniciado sesión
def login_required(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        username = get_session_username()
        user = get_user_by_username(username)

        if not user or user.status != 1:
            return render_template('user_inactive.html'), 403

        return view(*args, **kwargs)

    return decorated_view


# Función para redirigir al inicio si ya ha inciado sesión
def already_logged_in(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        if 'username' in session:
            return redirect(url_for('home.new_home'))

        return view(*args, **kwargs)

    return decorated_view
