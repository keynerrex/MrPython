# routes/home.py
from flask import (Blueprint, render_template, request,
                   session, redirect, url_for, jsonify)
from utils.decorators.decorators import already_logged_in, get_user_by_username


homes_routes = Blueprint('home', __name__)


@homes_routes.route('/', methods=['GET', 'POST'])
def index():
    return render_template('web_total.html')


@homes_routes.route('/cerrar', methods=['GET', 'POST'])
def cerrar_sesion():
    if 'username' in session and 'rol_user' in session:
        session.pop('username')
        session.pop('rol_user')

    return redirect(url_for('home.login_new'))


@homes_routes.route(f'/new_home', methods=['GET', 'POST'])
def new_home():
    return render_template('new_home.html'), 200


@homes_routes.route('/iniciar', methods=['GET', 'POST'])
@already_logged_in
def login_new():
    try:
        if request.method == 'POST':
            # Obtener los datos del formulario
            username = request.form.get('username')
            password = request.form.get('password', '')

            # Buscar el usuario en la base de datos por nombre de usuario
            user = get_user_by_username(username)

            if user and user.verify_password(password):
                # Verificar el estado del usuario
                if user.status != 1:
                    return jsonify({'error': 'Usuario inactivo'}), 403

                # Autenticación exitosa, establecer variables de sesión
                session['username'] = user.username.lower()
                session['rol_user'] = user.rol.rol if user.rol else None

                # Redirigir al usuario al inicio
                return jsonify({'CodeResponse': 200,
                                'success': 'Inicio exitoso',
                                'redirect_url': url_for('home.new_home')})

            else:
                return jsonify({
                    'CodeResponse': 400,
                    'error': 'Usuario o contraseña incorrectas'
                })

        # Renderizar el formulario de inicio de sesión
        return render_template('login_new.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400
