from flask import Flask, render_template, request, make_response, session
from flask import redirect, url_for, flash
from flask_wtf import CSRFProtect
import cookies_form
import logging as log
import json
import hashlib

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
csrf = CSRFProtect(app)
# Flask genera un token para prevenir ataques


@app.route('/')
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
    print("before")
    # if 'username' not in session and request.endpoint not in ['index']:
    #   print("username")
    # return redirect
    # print(request.endpoint)
    # print("El usuario necesita iniciar")


# After request - necesita un response
@app.after_request
def after_request(response):
    print("After")
    return response


@app.route('/cookies')
def cookies():
    title = 'Cookies'
    response = make_response(render_template('cookie.html', title=title))
    response.set_cookie('mi cookie', 'Keyner')
    return response


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


@app.route('/cookies/formulario', methods=['GET', 'POST'])
def comment():
    head = """
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
    />
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script
      src="https://code.jquery.com/jquery-3.6.4.js"
      integrity="sha256-a9jBBRygX1Bh5lt8GZjXDzyOB+bWve9EiO7tROUtj/E="
      crossorigin="anonymous"
    ></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <title>Cookies Formulario</title>
    </head>
    </html>
    """
    title = "Formularios"
    comment_form = cookies_form.ComentarForm(request.form)
    # El request es la solicitud HHTP, es decir al enviar y valida los campos
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        response = f"""
        {head}
        <div class="alert alert-success" role="alert">
        <label>Usuario:</label>
        <input type="text" disabled placeholder="{comment_form.username.data}" > <br>
        <label>Correo:</label>
        <input type="email" disabled placeholder="{comment_form.email.data}" ><br>
        <label>Mensaje:</label>
        <textarea name="mensaje" disabled> {comment_form.comment.data} </textarea><br>
        <script>
        Swal.fire(
        'Datos',
        'Usuario: {comment_form.username.data}<br>Correo: {comment_form.email.data}<br>Mensaje: {comment_form.comment.data}',
        'success'
        );
        </script>
        </div>
        """
        return response, log.info(f"Usuario: {comment_form.username.data}, Comentario: {comment_form.comment.data} ")
    else:
        return render_template('cookie.html', title=title, form=comment_form)


@app.route('/cerrar')
def cerrar_sesion():
    if 'username' in session:
        # Se ellimina la variable de username dentro de la sesion
        session.pop('username')
    # Poner el nombre de la funcion
    # Lo redireccionamos para que inicie sesion
    return redirect(url_for('login'))


@app.errorhandler(404)
def pagina_no_encontrada(error):
    cod_error = 404
    return render_template('notfound.html'), cod_error


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


if __name__ == "__main__":
    app.run(port=8000, debug=True)
