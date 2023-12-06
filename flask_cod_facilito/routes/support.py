from flask import (Blueprint, render_template,
                   request, redirect, url_for, flash)
from config.config import ProductionConfig
from werkzeug.utils import secure_filename
from models import db, Support
import os
from sqlalchemy.exc import IntegrityError
support_routes = Blueprint('support', __name__)
path_url = '/soporte/'


@support_routes.route(f'{path_url}enviar-soporte', methods=['GET', 'POST'])
def support_ticket():
    """Función para crear un ticket de soporte"""

    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form.get('username', 'Sin usuario')
        details_error = request.form.get('details_error')
        email = request.form.get('email', 'No se ha adjuntado un correo')
        image_path = None

        if not email:
            flash('Error: El correo es obligatorio', 'error',)
        elif not details_error:
            flash('Error: Es necesario llenar el detalle', 'error')

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

        if details_error and email:
            if image_path is None:
                image_path = 'No se adjunto ninguna imagen'
            try:
                support = Support(
                    username=username, details_error=details_error, image_path=image_path, email=email)
                # Agregar la instancia a la sesión y guardar en la base de datos
                db.session.add(support)
                db.session.commit()

                # Redireccionar a una nueva página después del envío exitoso
                flash('¡Ticket de soporte creado exitosamente!', 'success')
                return redirect(url_for('support.support_ticket'))

            except IntegrityError as ie:
                flash('Error: Se produjo un problema con la base de datos.', 'error')
                print(f"Ha ocurrido un error: {ie}")

            except TypeError as e:
                flash(
                    'Error: Se produjo un problema durante el procesamiento del formulario.', 'error')
                print(f"Sucedió un problema{e}")

            finally:
                db.session.rollback()
                db.session.close()

    return render_template('support_ticket.html', title='Soporte'), 200
