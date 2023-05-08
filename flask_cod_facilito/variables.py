from flask import Flask, render_template

app = Flask(__name__)
# Si quiero usar mi propia carpeta de template
# app = Flask(__name__, template_folder='folder_template')


@app.route('/variables/user/<name>')
def user(name='ej:'):
    age = 19
    lista = [1, 2, 3, 4]
    return render_template('variables.html', nombre=name, age=age, lista=lista)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
