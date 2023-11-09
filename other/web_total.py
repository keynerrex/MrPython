from werkzeug.security import generate_password_hash
from flask import (Flask, render_template, request,
                   make_response, session, redirect, url_for, flash, Blueprint)
from flask_wtf import CSRFProtect
from configs import config_general
from models.general import (db, User, Comment, Rol,
                            Registers, Types_id, Medias)
from flask_mail import (Mail, Message)
from functools import wraps
import web_form
import json
import hashlib
import locale
from routes.home import home_routes

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
app = Flask(__name__)
app.config.from_object(config_general.DevelopmentConfig)
app.register_blueprint(home_routes)
csrf = CSRFProtect()
mail = Mail()


@app.route('/', methods=['GET', 'POST'])
def index():
    title = 'Desarrollo con Flask'
    return render_template('web_total.html', title=title)


def admin_role_required(adm_user):
    @wraps(adm_user)
    def decorated_function(*args, **kwargs):
        username = session.get('username')
        rol_administrador = db.session.query(User.username, Rol.rol)\
            .join(Rol).filter(
                User.username == username,
                Rol.rol == 'Administrador').first()

        if not rol_administrador:
            return inauthorized()

        return adm_user(*args, **kwargs)

    return decorated_function


@app.errorhandler(401)
def inauthorized():
    code_err = 401
    return render_template('inauthorized.html', code_err=code_err), code_err


@app.before_request
def verify_session():

    if 'username' not in session and request.endpoint in ['comment_to_form']:
        return redirect(url_for('login'))

    elif 'username' in session and request.endpoint in ['login', 'form_to_database']:
        return redirect(url_for('index'))


@app.after_request
def after_request(response):
    return response


@app.route('/cookies')
def cookies():
    title = 'Cookies'
    response = make_response(render_template('cookie.html', title=title))
    response.set_cookie('mi cookie', 'Keyner')
    return response


@app.route('/crear-rol', methods=['GET', 'POST'])
@admin_role_required
def add_rol():
    if 'username' not in session:
        return redirect(url_for('login'))

    title = 'Crear roles'
    rol_form = web_form.AddRolForm(request.form)

    if request.method == 'POST' and rol_form.validate():
        rol_ = Rol(
            rol=rol_form.rol.data.capitalize())

        db.session.add(rol_)
        db.session.commit()
        return redirect(url_for('response_rol',
                                rol=rol_form.rol.data))

    return render_template('add_rol.html',
                           title=title,
                           form=rol_form)


@app.route('/response_rol', methods=['GET'])
def response_rol():
    rol = request.args.get('rol').capitalize()
    return render_template('response_rol.html',
                           title="Datos Recibidos",
                           rol=rol)


@app.route('/usuarios-registrados', methods=['GET'])
@admin_role_required
def users_registers():
    title = 'Usuarios registrados'
    users_per_page = 5
    page = request.args.get('page', 1, type=int)

    users = User.query.with_entities(User.username,
                                     User.email,
                                     User.status,
                                     User.create_date).paginate(
        page=page, per_page=users_per_page)
    total_pages = users.pages

    formated_users_registers = []
    for user in users.items:
        formatted_users_registers = user.create_date.strftime(
            "%A %d De %B Del %Y")

        formated_users_registers.append(formatted_users_registers.encode(
            'latin-1').decode('utf-8').capitalize())

    return render_template('users-registers.html',
                           title=title,
                           users=users,
                           formated_users_registers=formated_users_registers,
                           total_pages=total_pages)


@app.route('/roles-creados', methods=['GET'])
@admin_role_required
def show_roles():
    title = 'Roles Creados'
    rol_per_page = 5
    page = request.args.get('page', 1, type=int)

    roles = Rol.query.with_entities(Rol.rol,
                                    Rol.create_date,
                                    Rol.status).paginate(
        page=page, per_page=rol_per_page)

    formated_roles = []
    for rol in roles.items:
        formatted_roles = rol.create_date.strftime("%A %d De %B Del %Y")
        formated_roles.append(formatted_roles.encode(
            'latin-1').decode('utf-8').capitalize())

    total_pages = roles.pages
    return render_template('roles.html',
                           title=title,
                           roles=roles,
                           formatted_roles=formated_roles,
                           total_pages=total_pages)


@app.route('/ingresar', methods=['GET', 'POST'])
def login():
    title = "Iniciar sesión"
    login_form = web_form.LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(username=username).first()

        if user and user.verify_password(password):
            success_message = f"Bienvenido {username}, pasela bien"
            flash(success_message)
            session['username'] = username

            return redirect(url_for('home.index'))
        else:
            error_message = "Usuario o contraseña no validos"
            flash(error_message)

    return render_template('login_web.html', title=title, form=login_form)


@app.route('/escribir-comentario', methods=['GET', 'POST'])
def comment_to_form():
    if 'username' not in session:
        return redirect(url_for('login'))

    title = "Escribir comentario"
    username = session['username']

    current_user = User.query.filter_by(username=username).first()
    email = current_user.email if current_user else None

    comment_form = web_form.ComentarForm(request.form)

    if request.method == 'POST' and comment_form.validate():
        comment = Comment(
            username=username,
            comment=comment_form.comment.data)

        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('response_web_form',
                                username=username,
                                email=email,
                                comment=comment_form.comment.data))

    else:
        return render_template('comment_user.html',
                               title=title,
                               form=comment_form,
                               username=username,
                               email=email)


@app.route('/response_web_form', methods=['GET'])
def response_web_form():
    username = request.args.get('username')
    email = request.args.get('email')
    comment = request.args.get('comment')

    return render_template('response_web_form.html',
                           title="Datos Recibidos",
                           username=username,
                           email=email,
                           comment=comment)


@app.route('/formulario-ingreso', methods=['GET', 'POST'])
def form_to_database():
    title = "Formulario de ingreso"
    create_formulario = web_form.CreateForm(request.form)

    if request.method == 'POST' and create_formulario.validate():
        user = User(create_formulario.username.data,
                    create_formulario.password.data,
                    create_formulario.email.data)

        db.session.add(user)
        db.session.commit()

        message = Message('Te has registrado en Flask',
                          sender=app.config['MAIL_USERNAME'],
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


@app.route('/mis-comentarios', methods=['GET', 'POST'])
def my_comments():
    if 'username' not in session:
        return redirect(url_for('login'))

    title = 'Mis Comentarios'
    my_comments_per_page = 5
    page = request.args.get('page', 1, type=int)

    username = session['username']
    current_user = User.query.filter_by(
        username=username).first()

    comments = Comment.query.with_entities(
        Comment.username,
        Comment.comment,
        Comment.create_date
    ).filter_by(username=current_user.username).paginate(
        page=page, per_page=my_comments_per_page)

    formatted_comments = []
    for comment in comments.items:
        formatted_date = comment.create_date.strftime("%A %d De %B Del %Y")
        formatted_comments.append(formatted_date.encode(
            'latin-1').decode('utf-8').capitalize())

    return render_template('my-comments.html',
                           title=title,
                           my_comments=comments,
                           formatted_comments=formatted_comments)


@app.route('/comentarios-usuarios', methods=['GET'])
def show_comments():
    title = 'Comentarios de usuarios'
    users_per_page = 5
    page = request.args.get('page', 1, type=int)

    comments = Comment.query.with_entities(Comment.username,
                                           Comment.comment,
                                           Comment.create_date).paginate(
        page=page, per_page=users_per_page)
    total_pages = comments.pages

    formatted_usr_comments = []
    for comment_user in comments.items:
        formatted_date = comment_user.create_date.strftime(
            "%A %d De %B Del %Y")

        formatted_usr_comments.append(
            formatted_date.encode('latin-1').decode('utf-8').capitalize())

    return render_template('comentarios-usuarios.html',
                           title=title,
                           comments=comments,
                           formatted_usr_comments=formatted_usr_comments,
                           total_pages=total_pages)


@app.route('/registrarme', methods=['GET', 'POST'])
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
            return redirect(url_for('response_registers'))

    return render_template('registers.html',
                           title=title,
                           types=types,
                           medias=medias)


@app.route('/response_register', methods=['GET'])
def response_registers():

    return render_template('response_registers.html',
                           title='Datos registrados')


@app.route('/cerrar', methods=['GET', 'POST'])
def cerrar_sesion():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))


@app.route('/restablecer-clave', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        username = request.form.get('username', '')
        pass_reset = generate_password_hash('123456')
        user = User.query.filter_by(username=username).first()

        if user:
            user.password = pass_reset
            db.session.commit()
            return redirect(url_for('response_general'))
        else:
            flash('Usuario no encontrado')

    return render_template('reset_password.html')


@app.route('/response-clave', methods=['GET'])
def response_general():
    url = '/'
    h3 = 'Restablecimiento de clave exitoso'
    title_swal = 'Se ha restablecido la contraseña'
    message_swal = 'Contraseña restablecida exitosamente'

    return render_template('response_general.html',
                           url=url,
                           h3=h3,
                           title_swal=title_swal,
                           message_swal=message_swal)


@app.errorhandler(404)
def page_not_found(error):
    cod_error = 404
    return render_template('notfound.html'), cod_error


@app.route('/ajax-login', methods=['POST'])
def ajax_login():
    username = request.form['username']
    password = request.form['password']

    encript_pass = hashlib.sha256(password.encode()).hexdigest()
    response = {'status': 200, 'username': username,
                'password': encript_pass, 'id': 1}

    return json.dumps(response)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=80, debug=True)
