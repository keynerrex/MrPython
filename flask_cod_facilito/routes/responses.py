from flask import Blueprint, render_template, url_for

responses_routes = Blueprint('responses', __name__)


@responses_routes.route('/response-clave', methods=['GET'])
def response_password():
    url = url_for('passwords.reset_password')
    h3 = 'Restablecimiento de clave exitoso'
    title_swal = 'Se ha restablecido la contraseña'
    message_swal = 'Contraseña restablecida exitosamente'

    return render_template('response_general.html',
                           url=url,
                           h3=h3,
                           title_swal=title_swal,
                           message_swal=message_swal,
                           icon='success')


@responses_routes.route('/response_register', methods=['GET'])
def response_registers():

    return render_template('response_registers.html',
                           title='Datos registrados')
