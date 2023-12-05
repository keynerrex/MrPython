from flask import (Blueprint, render_template, request)
from config.config import ProductionConfig
from werkzeug.utils import secure_filename
from models import db, Support
import os


support_routes = Blueprint('support', __name__)
path_url = '/soporte/'


@support_routes.route(f'{path_url}enviar-soporte', methods=['GET', 'POST'])
def support_ticket():
    """Función para crear un ticket de soporte"""

    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form.get('username', 'Sin usuario')
        details_error = request.form.get('details_error')
        image_path = None

        # Verificar si se ha subido una imagen
        if 'image_error' in request.files:
            image_file = request.files['image_error']

            if image_file.filename != '':
                upload_folder = ProductionConfig.UPLOAD_FOLDER

                # Asegúrate de que el directorio de carga exista
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)

                # Guardar la imagen y obtener la ruta
                image_path = os.path.join(
                    upload_folder, secure_filename(image_file.filename))
                image_file.save(image_path)
                print('Se ha guardado la imagen en:', image_path)

        # Si se guardó la imagen, almacenar los datos en la base de datos
        if image_path is not None:
            # Crear una instancia de Support con los datos del formulario
            support = Support(
                username=username, details_error=details_error, image_path=image_path, status=1)

            # Agregar la instancia a la sesión y guardar en la base de datos
            db.session.add(support)
            db.session.commit()

    return render_template('support_ticket.html')
