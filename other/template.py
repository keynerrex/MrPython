from flask import Flask, render_template

app = Flask(__name__)
# Si quiero usar mi propia carpeta de template
# app = Flask(__name__, template_folder='folder_template')


@app.route('/template')
def index():
    # Todo lo agarra del template
    return render_template('index.html')


@app.route('/prueba/')
def render_prueba():
    return render_template('prueba.html')


@app.errorhandler(404)
def pagina_no_encontrada(error):
    cod_error = 404
    return render_template('notfound.html'), cod_error


if __name__ == '__main__':
    app.run(port=8000, debug=True)
