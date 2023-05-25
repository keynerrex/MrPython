from flask import Flask, render_template, request, make_response
from flask_wtf import CSRFProtect
import formularios_form
import logging as log


app = Flask(__name__)
app.secret_key = 'keynerrex', 'Indefined'
csrf = CSRFProtect(app)

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log', encoding='utf-8'),
                    log.StreamHandler()
                ])


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = "Login Formulario"
    login_form = formularios_form.LoginForm(request.form)

    return render_template('login.html', title=title, form=login_form)


@app.route('/cookie', methods=['GET', 'POST'])
def cookie():
    title = 'Cookies formulario'
    response = make_response(render_template('web_total.html', title=title))
    response.set_cookie('mi cookie', 'cooki_')

    return response


@app.route('/formularios', methods=['GET', 'POST'])
def formularios():
    title = "Formularios"
    comment_form = formularios_form.ComentarForm(request.form)
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
    return render_template('formularios.html', title=title, form=comment_form)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
