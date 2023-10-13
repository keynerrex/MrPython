# Usa una imagen base de Python
FROM python:3.9


# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements/requirements.txt /app

# Instala las dependencias desde el archivo requirements.txt
RUN pip install -r requirements.txt

# Copia el resto de los archivos y carpetas de tu aplicación al contenedor
COPY . /app

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 8000

# Comando para ejecutar tu aplicación
CMD ["python", "web_total.py"]
