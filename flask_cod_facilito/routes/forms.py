from flask import Blueprint, render_template, request, current_app, url_for, redirect, flash
from utils.decorators.decorators import already_logged_in
from forms.web_form import CreateForm
from models.general import (db, User, Types_id, Medias, Registers)
from config.mail import mail, Message

forms_routes = Blueprint('forms', __name__)


@forms_routes.route('/formulario-ingreso', methods=['GET', 'POST'])
@already_logged_in
def form_to_database():
    title = "Formulario de ingreso"
    create_formulario = CreateForm(request.form)

    if request.method == 'POST' and create_formulario.validate():
        user = User(create_formulario.username.data,
                    create_formulario.password.data,
                    create_formulario.email.data)

        db.session.add(user)
        db.session.commit()

        message = Message('Te has registrado en Flask',
                          sender=current_app.config['MAIL_USERNAME'],
                          recipients=[user.email])

        message.html = render_template('email.html',
                                       user=user.username)
        mail.send(message)

        response = render_template('response_databases.html',
                                   title="Usuario registrado",
                                   username=user.username,
                                   email=user.email)
        return response
    return render_template('formulario-ingreso.html',
                           form=create_formulario,
                           title=title)


@forms_routes.route('/registrarme', methods=['GET', 'POST'])
@already_logged_in
def registers():
    title = 'Registrarme'
    types = db.session.query(Types_id).order_by(Types_id.type_id.asc()).all()
    medias = db.session.query(Medias).order_by(Medias.media_id.asc()).all()

    if request.method == 'POST':
        fullname = request.form.get('fullname')
        type_id = request.form.get('type_id')
        num_id = request.form.get('num_id')
        email = request.form.get('email')
        phone = request.form.get('phone')
        media_id = request.form.get('media_id')

        if len(fullname) < 5:
            flash('El nombre es muy corto, debe tener al menos 5 caracteres')
        elif "@" not in email:
            flash('El email no es valido')
        elif len(phone) != 10:
            flash('Numero invalido')
        elif len(num_id) < 7 or len(num_id) > 10:
            flash("Numero de identifación invalida")
        else:
            register = Registers(fullname=fullname,
                                 type_id=type_id,
                                 num_id=num_id,
                                 email=email,
                                 phone=phone,
                                 media_id=media_id)

            db.session.add(register)
            db.session.commit()
            return redirect(url_for('responses.response_registers'))

    return render_template('registers.html',
                           title=title,
                           types=types,
                           medias=medias)
