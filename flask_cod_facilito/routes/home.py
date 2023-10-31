# routes/home.py
from flask import (Blueprint, render_template, request, flash,
                   session, redirect, url_for, make_response)
from utils.decorators.decorators import login_required, already_logged_in
from models.general import User, Rol, db
from forms.web_form import LoginForm
import random

homes_routes = Blueprint('home', __name__)


@homes_routes.route('/', methods=['GET', 'POST'])
def index():
    return render_template('web_total.html')


@homes_routes.route('/ingresar', methods=['GET', 'POST'])
@already_logged_in
def login():
    title = "Iniciar sesión"
    login_form = LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(username=username).first()
        rol_user = db.session.query(Rol.rol).join(User).filter(
            User.username == username).first()[0]

        print(rol_user)

        if user and user.verify_password(password):
            success_message = f"Bienvenido {username}, ¡pásela bien!"
            flash(success_message)
            session['username'] = username
            session['rol_user'] = rol_user

            cookie_value = random.randint(1, 10)
            response = make_response(redirect(url_for('home.index')))
            response.set_cookie('CookieName', str(cookie_value))

            return response

        else:
            error_message = "Usuario o contraseña no válidos"
            flash(error_message)

    return render_template('login_web.html', title=title, form=login_form)


@homes_routes.route('/cerrar', methods=['GET', 'POST'])
@login_required
def cerrar_sesion():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('home.login'))
