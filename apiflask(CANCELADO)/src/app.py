from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)
conn = MySQL(app)


@app.route('/curses', methods=['GET'])
def list_curses():
    try:
        cursor = conn.connection.cursor()
        sql = "SELECT * FROM curses"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos = []
        for fila in datos:
            curso = {
                'codigo': fila[1],
                'nombre': fila[2],
                'creditos': fila[3]
            }
            cursos.append(curso)
        print(cursos)
        return jsonify({'cursos': cursos, 'mensaje': 'Cursos listados'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


@app.route('/curses/<code>', methods=['GET'])
def curse(code):
    try:

        cursor = conn.connection.cursor()
        sql = "SELECT * FROM curses WHERE codigo=%s"
        # Si es solo un elemento, se le pone , al ser tupla
        value = (code,)
        cursor.execute(sql, value)
        datos = cursor.fetchone()
        if datos is not None:
            curso = {
                'codigo': datos[1],
                'nombre': datos[2],
                'creditos': datos[3]
            }
            return jsonify({'curso': curso, 'mensaje': 'Curso encontrado'})
        else:
            return jsonify({'mensaje': 'Curso no encontrado'})

    except Exception as err:
        return f"Error: {err}"


@app.route('/curses_add', methods=['POST'])
def add_course():
    try:
        cursor = conn.connection.cursor()
        sql = "INSERT INTO curses (codigo,nombre,creditos) VALUES (%s,%s,%s)"
        data = request.json
        values = (data.get('codigo'),
                  data.get('nombre'),
                  data.get('creditos'))
        cursor.execute(sql, values)
        conn.connection.commit()
        return jsonify({'mensaje': 'Curso registrado.'})

    except Exception as ex:
        print(f"Error: {ex}")
        return jsonify({'mensaje': 'Error'})


@app.errorhandler(404)
def not_found(error):
    cod_error = 404
    return f"Pagina no encontrada", cod_error


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(port=8000)
