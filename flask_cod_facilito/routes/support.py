from flask import (Blueprint, render_template)
from utils.decorators.decorators import no_available


support_routes = Blueprint('support', __name__)
path_url = '/soporte/'


@support_routes.route(f'{path_url}enviar-soporte', methods=['GET', 'POST'])
@no_available
def support_ticket():
    return render_template('support_ticket.html')
