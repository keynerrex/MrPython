from flask import Blueprint, render_template
from utils.decorators import role_required

config_routes = Blueprint('config', __name__)
path_url = '/configuracion/'


@config_routes.route(f'{path_url}utilidades', methods=['GET'])
@role_required('Administrador')
def home_config():
    return render_template('configuracion.html')
