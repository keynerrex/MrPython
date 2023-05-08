from flask import Flask, render_template, request, make_response, session
from flask import redirect, url_for, flash
from flask_wtf import CSRFProtect
import cookies_form
import logging as log
import json


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
    title = "Formularios"
    comment_form = cookies_form.ComentarForm(request.form)
    # El request es la solicitud HHTP, es decir al enviar y valida los campos
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        response = f"""
        <label>Usuario:</label>
        <input type="text" disabled placeholder="{comment_form.username.data}" > <br>
        <label>Correo:</label>
        <input type="email" disabled placeholder="{comment_form.email.data}" ><br>
        <label>Mensaje:</label>
        <textarea name="mensaje" disabled> {comment_form.comment.data} </textarea><br>
        """
        return response, log.info(f"Usuario: {comment_form.username.data}, Comentario: {comment_form.comment.data} ")
    else:
        error = "Error en el formulario"
        log.error(f"Error en el formulario: {error}")
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
    print(request.form)
    username = request.form['username']
    response = {'status': 200, 'username': username, 'id': 1}
    # Pasar diccionario a json
    return json.dumps(response)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
