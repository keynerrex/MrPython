from flask import Flask, render_template
from config.config import ProductionConfig
from flask_wtf import CSRFProtect
from config.mail import mail
from models.general import db
from routes import (home_route,
                    user_route,
                    rol_route,
                    comment_route,
                    password_route,
                    response_route,
                    form_route)


csrf = CSRFProtect()
app = Flask(__name__)


# Rutas generales
@app.errorhandler(404)
def page_not_found(error):
    cod_error = 404
    return render_template('notfound.html'), cod_error


def create_app():
    app.config.from_object(ProductionConfig)

    db.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)

    app.register_blueprint(home_route)
    app.register_blueprint(user_route)
    app.register_blueprint(rol_route)
    app.register_blueprint(comment_route)
    app.register_blueprint(password_route)
    app.register_blueprint(response_route)
    app.register_blueprint(form_route)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)
