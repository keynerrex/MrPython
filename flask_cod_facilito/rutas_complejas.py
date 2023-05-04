from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hola rutas_complejas.py"


@app.route('/params/<nombre>')
def params(nombre):
    # nombre = request.args.get('nombre', 'no asignó un nombre')
    return f"Nombre: {nombre}"

# Pasar string y numeros


@app.route('/params/<nombre>/<int:edad>')
def params_(nombre, edad):
    return f"Nombre: {nombre}, edad: {edad}"


if __name__ == '__main__':
    app.run(port=8000, debug=True)
