from flask import flash, render_template, request, redirect, url_for, Blueprint, session
from models.general import db, User
from werkzeug.security import generate_password_hash
from utils.decorators.decorators import admin_role_required, already_logged_in, login_required

passwords_routes = Blueprint('passwords', __name__)


@passwords_routes.route('/restablecer-contraseña', methods=['GET', 'POST'])
@login_required
@admin_role_required
def reset_password():
    title = 'Restablecer contraseñas'
    if request.method == 'POST':
        username = request.form.get('username', '')
        pass_reset = generate_password_hash('123456')
        user = User.query.filter_by(username=username).first()

        if user:
            user.password = pass_reset
            db.session.commit()
            return redirect(url_for('responses.response_password'))
        else:
            flash('Usuario no encontrado')

    return render_template('reset_password.html', title=title)


@passwords_routes.route('/cambiar-contraseña', methods=['GET', 'POST'])
@login_required
def change_password():
    title = 'Cambiar contraseña'

    if request.method == 'POST':
        username = session.get('username')
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        verify_password = request.form.get('verify_password')

        user = User.query.filter_by(username=username).first()

        if user.verify_password(current_password):
            if verify_password == new_password:
                user.password = generate_password_hash(new_password)
                db.session.commit()
                flash('Contraseña cambiada exitosamente')
            else:
                flash('Las contraseñas no coinciden')
        else:
            flash('La contraseña actual no es válida')

    return render_template('change_password.html', title=title)
