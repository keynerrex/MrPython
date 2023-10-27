from flask import Blueprint, render_template

loading_routes = Blueprint('loading', __name__)


@loading_routes.route('/loading', methods=['GET'])
def loading():
    return render_template('loading.html')
