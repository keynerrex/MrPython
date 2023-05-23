from flask import (Flask, render_template, request,
                   make_response, session,
                   redirect, url_for, flash, globals, jsonify)
from flask_wtf import CSRFProtect
from flask_login import current_user
from config import DevelopmentConfig
from models import db, User, Comment
from flask_mail import (Mail, Message)
import cookies_form
import logging as log
import json
import hashlib

# Configuracion de loggin
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log', encoding='utf-8'),
                    log.StreamHandler()
                ])

app = Flask(__name__)
# Usar las configuraciones de mi clase
app.config.from_object(DevelopmentConfig)
# (Cross-Site Request Forgery)
# Flask genera un token para prevenir ataques
# -Ya no pasamos la app, lo hace abajo
csrf = CSRFProtect()
mail = Mail()


# Vista alternativa principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        username = session['username']
        print(username)
    mi_cookie = request.cookies.get('mi cookie', 'Undefined')
    print(mi_cookie)
    title = 'Cookies'
    return render_template('cookies.html', title=title)


# Before request
@app.before_request
def verify_session():

    # Esto verificara que se haya iniciado sesion, para asi poder ir a la funcion comentario_to_formulario
    if 'username' not in session and request.endpoint in ['comentario_to_formulario']:
        return redirect(url_for('login'))
    # Si el usuario inicio lo redirecciona a la funcion del index
    elif 'username' in session and request.endpoint in ['login', 'formulario_to_database']:
        return redirect(url_for('index'))


@app.after_request
def after_request(response):
    return response


# Vista principal
@app.route('/cookies')
def cookies():
    title = 'Cookies'
    response = make_response(render_template('cookie.html', title=title))
    response.set_cookie('mi cookie', 'Keyner')
    return response


# Vista de inicio de sesion
@app.route('/login', methods=['GET', 'POST'])
def login():
    title = "Login Cookie"
    login_form = cookies_form.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():

        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password):
            success_message = f"Bienvenido {username}, pasela bien"
            print(success_message)
            flash(success_message)
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error_message = "Usuario o contraseña no validos"
            print(error_message)
            flash(error_message)

    return render_template('login_cookie.html', title=title, form=login_form)


# Ruta del formulario
@app.route('/comentario-usuario', methods=['GET', 'POST'])
def comentario_to_formulario():
    # Verificar si el usuario ha iniciado sesión
    if 'username' not in session:
        return redirect(url_for('login'))

    # Datos que e envian
    title = "Formularios"
    username = session['username']
    usuario_actual = User.query.filter_by(username=username).first()
    email = usuario_actual.email if usuario_actual is not None else None

    # Crear una instancia del formulario de comentarios con los datos del usuario
    comment_form = cookies_form.ComentarForm(
        request.form)

    # Si se envió el formulario por el método POST y es válido
    if request.method == 'POST' and comment_form.validate():

        # Crear un objeto Comment con los datos del formulario
        comment = Comment(
            username=username,
            comment=comment_form.comment.data
        )

        # Agregar el comentario a la base de datos
        db.session.add(comment)
        db.session.commit()

        # Redirigir a la vista de respuesta y pasar los datos del comentario en la URL
        return redirect(url_for('response_cookies_form',
                                username=username,
                                email=email,
                                comment=comment_form.comment.data))

    else:
        # Si no se envió el formulario por el método POST o no es válido, mostrar el formulario nuevamente
        return render_template('comment_user.html', title=title, form=comment_form, username=username, email=email)


# Vista de respuesta después de enviar el formulario
@app.route('/response_cookies_form', methods=['GET'])
def response_cookies_form():
    # Obtener los datos del comentario de la URL
    username = request.args.get('username')
    email = request.args.get('email')
    comment = request.args.get('comment')

    # Mostrar la plantilla de respuesta con los datos del comentario
    return render_template('response_cookies_form.html', title="Datos Recibidos", username=username, email=email, comment=comment)


@ app.route('/formulario-ingreso', methods=['GET', 'POST'])
def formulario_to_database():
    title = "Formulario de ingreso"
    create_formulario = cookies_form.CreateForm(request.form)
    if request.method == 'POST' and create_formulario.validate():

        # Se obtienen los datos del POST previo del envio
        user = User(create_formulario.username.data,
                    create_formulario.password.data,
                    create_formulario.email.data
                    )

        # Se hace la agregacion de la inyeccion
        db.session.add(user)
        # Y se ejecuta la inyeccion
        db.session.commit()

        message = Message('Te has registrado en Flask',
                          sender=app.config['MAIL_USERNAME'],
                          recipients=[user.email]
                          )
        message.html = render_template('email.html', user=user.username)
        mail.send(message)
        # Por ultimo damos una respuesta a que se ha insertado correctamente
        # Renderizando un html personalizado
        response = render_template('response_databases.html',
                                   title="Usuario registrado",
                                   username=user.username,
                                   email=user.email
                                   )
        return response, log.info(f"Usuario registrado: {user.username}")
    # Y esta funcion primero cargara el template antes que la condicion if
    return render_template('formulario-ingreso.html', form=create_formulario, title=title)

#Comentarios hechos por cada usuario
@app.route('/mis-comentarios', methods=['GET', 'POST'])
def my_comments():
    title = 'Mis Comentarios'
    username = session['username']
    usuario_actual = User.query.filter_by(username=username).first()
    comments_users = Comment.query.with_entities(
        Comment.username,
        Comment.comment
    ).filter_by(username=usuario_actual.username).all()
    
    print(f"hola: {usuario_actual.username}")
    return render_template('my-comments.html', title=title,
                           comments_users=comments_users)


@app.route('/comentarios-usuarios', methods=['GET'])
def show_comments():
    title = 'Comentarios de usuarios'
    comments_users = Comment.query.with_entities(
        Comment.username,
        Comment.comment
    ).all()
    # --Para pruebas
    comments = []
    for comment_user in comments_users:
        username = comment_user.username
        comment = comment_user.comment
        comments.append({'username': username, 'comment': comment})
        print(f"User: {username} : {comment}")
    # ----
    return render_template('comentarios-usuarios.html',
                           title=title,
                           comments_users=comments_users)


# Por ejemplo lo pongo porque quiero que desde un POST de otro html
# me renvie aca
@app.route('/cerrar', methods=['GET', 'POST'])
def cerrar_sesion():
    if 'username' in session:
        # Se elimina la variable de username dentro de la sesion
        session.pop('username')
    # Poner el nombre de la funcion
    # Lo redireccionamos para que inicie sesion
    return redirect(url_for('login'))


# Vista de pagina no encontrada
@ app.errorhandler(404)
def pagina_no_encontrada(error):
    cod_error = 404
    return render_template('notfound.html'), cod_error


# Prueba de muestreo con json y js-jquery-ajax
@ app.route('/ajax-login', methods=['POST'])
def ajax_login():
    username = request.form['username']
    password = request.form['password']
    # Encriptacion
    encript_pass = hashlib.sha256(password.encode()).hexdigest()
    response = {'status': 200, 'username': username,
                'password': encript_pass, 'id': 1}

    log.info(f"Username[POST]: {username} Password[POST]: {password}")
    # Pasar diccionario a json
    return json.dumps(response)

# Correos


# Ejecución
if __name__ == "__main__":
    # Iniciar las configuraciones que ya tenemos
    csrf.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8000)
