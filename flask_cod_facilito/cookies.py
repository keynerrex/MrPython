from flask import (Flask, render_template, request,
                   make_response, session,
                   redirect, url_for, flash, globals)
from flask_wtf import CSRFProtect
import cookies_form
import logging as log
import json
import hashlib
from config import DevelopmentConfig
from models import db, User

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
def before_request():
    if 'username' not in session and request.endpoint in ['comentario_to_formulario']:
        return redirect(url_for('login'))
    elif 'username' in session and request.endpoint in ['login', 'create']:
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
# Test rama keynerrex
# TEST 2 RAMA
#TEST 3

# Ruta del formulario
@ app.route('/cookies/formulario', methods=['GET', 'POST'])
def comentario_to_formulario():
    # Se define el titulo que va tener
    title = "Formularios"
    # Intanciamos la clase de donde generara los inputs y sus validaciones
    comment_form = cookies_form.ComentarForm(request.form)
    # El request es la solicitud HTTP, es decir al enviar
    # y valida los campos
    if request.method == 'POST' and comment_form.validate():
        # Creamos una respuesta y renderizamos la plantilla donde nos mostrata los datos
        response = render_template('response_cookies_form.html',
                                   title="Datos Recibidos",
                                   username=comment_form.username.data,
                                   email=comment_form.email.data,
                                   comment=comment_form.comment.data
                                   )
        # Retornamos y guardamos en el log:
        # (Solo usar para registrar errores detallados)
        return response, log.info(f"Usuario: {comment_form.username.data}, Comentario: {comment_form.comment.data} ")
    else:
        # Si no es un envio POST, retornamos a la misma vista
        return render_template('cookie.html', title=title, form=comment_form)


@ app.route('/formulario-ingreso', methods=['GET', 'POST'])
def formulario_to_database():
    title = "Formulario de ingreso"
    create_formulario = cookies_form.CreateForm(request.form)
    if request.method == 'POST' and create_formulario.validate():

        user = User(create_formulario.username.data,
                    create_formulario.password.data,
                    create_formulario.email.data
                    )

        db.session.add(user)
        db.session.commit()

        response = render_template('response_databases.html',
                                   title="Usuario registrado",
                                   username=user.username,
                                   password=user.password,
                                   email=user.email
                                   )
        return response, log.info(f"Usuario registrado: {user.username}")
    return render_template('formulario-ingreso.html', form=create_formulario, title=title)


# Por ejemplo lo pongo porque quiero que desde un POST de otro html
# me renvie aca
@ app.route('/cerrar', methods=['GET', 'POST'])
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


# Ejecución
if __name__ == "__main__":
    # Iniciar las configuraciones que ya tenemos
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8000)
