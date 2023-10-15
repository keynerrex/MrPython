from flask import Flask, render_template

app = Flask(__name__)
# Si quiero usar mi propia carpeta de template
# app = Flask(__name__, template_folder='folder_template')


@app.route('/extends')
def index():
    return render_template('extends.html')

# @app.route('/user/<name>')
# def user(name='ej:'):
#     return render_template('extends.html', nombre=name)


@app.route('/clientes')
def clientes():
    lista_nombres = ['keyner', 'Santiago', 'Oliveros', 'Florez']
    return render_template('clientes.html', lista_nombres=lista_nombres)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
