from flask import Blueprint, render_template
from utils.decorators.decorators import no_available

loading_routes = Blueprint('loading', __name__)


@loading_routes.route('/loading', methods=['GET'])
@no_available
def loading():
    return render_template('loading.html')
