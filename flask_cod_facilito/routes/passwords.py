from flask import flash, render_template, request, redirect, url_for, Blueprint
from models.general import db, User
from werkzeug.security import generate_password_hash

passwords_routes = Blueprint('passwords', __name__)


@passwords_routes.route('/restablecer-clave', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        username = request.form.get('username', '')
        pass_reset = generate_password_hash('123456')
        user = User.query.filter_by(username=username).first()

        if user:
            user.password = pass_reset
            db.session.commit()
            return redirect(url_for('responses.response_clave'))
        else:
            flash('Usuario no encontrado')

    return render_template('reset_password.html')
