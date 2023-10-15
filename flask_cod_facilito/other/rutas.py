from flask import Flask, request

app = Flask(__name__)


@app.route('/rutas')
def index():
    return "Hola rutas.py"


@app.route('/bienvenido')
def bienvenido():
    return "Bienvenido"


@app.route('/params')
def params():
    # Devuelve default en caso no tener
    params = request.args.get('params1', 'no tiene este parametro')
    params2 = request.args.get('params2', 'no tiene este parametro')
    return f"Parametos: {params}, {params2}"
# Se le puede pasar un parametro /params?params1=keyner
# http://127.0.0.1:8000/params?params1=keyner&params2=kin


if __name__ == '__main__':
    app.run(port=8000, debug=True)
