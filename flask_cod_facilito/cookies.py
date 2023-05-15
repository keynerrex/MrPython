from flask import (Flask, render_template, request,
                   make_response, session,
                   redirect, url_for, flash, globals)
from flask_wtf import CSRFProtect
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

# (Cross-Site Request Forgery)
app.secret_key = "mi_llave"
# Flask genera un token para prevenir ataques
csrf = CSRFProtect(app)


# Vista alternativa principal
@app.route('/')
def index():
    print(globals.test)
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
    # Variable global
    globals.test = 'test'
    print("before")


# After request - necesita un response
@app.after_request
def after_request(response):
    print(globals.test)
    print("After")
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
    if login_form == 'POST' and login_form.validate():
        username = login_form.username.data
        # Crear mensaje
        success_message = f'Bienvenido: {username}'
        # Enviar mensaje al cliente
        flash(success_message, 'success')
        session['username'] = login_form.username.data
        # success = log.info(f" Usuario: {login_form.username}")
        return redirect(url_for('index'))

    return render_template('login_cookie.html', title=title, form=login_form)


# Ruta del formulario
@app.route('/cookies/formulario', methods=['GET', 'POST'])
def comentario_to_formulario():
    # Se define el titulo que va tener
    title = "Formularios"
    # Intanciamos la clase de donde generara los inputs y sus validaciones
    comment_form = cookies_form.ComentarForm(request.form)
    # El request es la solicitud HTTP, es decir al enviar y valida los campos
    if request.method == 'POST' and comment_form.validate():
        # Creamos una respuesta y renderizamos la plantilla donde nos mostrata los datos
        response = render_template('response_cookies_form.html',
                                   title="Datos Recibidos",
                                   username=comment_form.username.data,
                                   email=comment_form.email.data,
                                   comment=comment_form.comment.data
                                   )
        # Retornamos y guardamos en el log:(Solo usar para registrar errores detallados)
        return response, log.info(f"Usuario: {comment_form.username.data}, Comentario: {comment_form.comment.data} ")
    else:
        # Si no es un envio POST, retornamos a la misma vista
        return render_template('cookie.html', title=title, form=comment_form)


@app.route('/cerrar')
def cerrar_sesion():
    if 'username' in session:
        # Se elimina la variable de username dentro de la sesion
        session.pop('username')
    # Poner el nombre de la funcion
    # Lo redireccionamos para que inicie sesion
    return redirect(url_for('login'))


# Vista de pagina no encontrada
@app.errorhandler(404)
def pagina_no_encontrada(error):
    cod_error = 404
    return render_template('notfound.html'), cod_error


# Prueba de muestreo con json y js-jquery-ajax
@app.route('/ajax-login', methods=['POST'])
def ajax_login():
    username = request.form['username']
    password = request.form['password']
    # Encriptacion
    encript_pass = hashlib.sha256(password.encode()).hexdigest()
    response = {'status': 200, 'username': username,
                'password': encript_pass, 'id': 1}
    # Pasar diccionario a json
    log.info(f"Username[POST]: {username} Password[POST]: {password}")
    return json.dumps(response)


# Ejecución
if __name__ == "__main__":
    app.run(port=8000, debug=True)
