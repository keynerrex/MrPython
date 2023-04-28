# Importar Flask y json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# Se hace la conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/bdpythonapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db para mapear las tablas
db = SQLAlchemy(app)
# ma para crear schema para un modelo de tabla
ma = Marshmallow(app)

# Creacion de la tabla categoria

# Se crea la clase de categoria


class Categoria(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))
    # inicializamos los datos que se piden en la tabla

    def __init__(self, cat_nom, cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp


# Acá para que flask sepa el contexto de la aplicacion
# Flask necesita el with
with app.app_context():
    db.create_all()

# Crear esquema con Marshmallow


class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria


categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)

# GET Devolviendo un json


@app.route('/Categorias', methods=['GET'])
def get_categorias():
    all_categorias = Categoria.query.all()
    result = categorias_schema.dump(all_categorias)
    return jsonify(result)

# GET POR id


@app.route('/Categorias/<int:id>', methods=['GET'])
def get_categorias_id(id):
    categoria = Categoria.query.get(id)
    if categoria:
        return categoria_schema.jsonify(categoria)
    else:
        return "Categoria no encontrada", 404

# POST -> se importa el request


@app.route('/Categoria', methods=['POST'])
def insert_categoria():
    data = request.get_json(force=True)
    cat_nom = data['cat_nom']
    cat_desp = data['cat_desp']

    nuevocategoria = Categoria(cat_nom, cat_desp)

    db.session.add(nuevocategoria)
    db.session.commit()
    return categoria_schema.jsonify(nuevocategoria)

# UPDATE PUT


@app.route('/Categoria/<id>', methods=['PUT'])
def update_categoria(id):
    actualizar_categoria = Categoria.query.get(id)

    if not actualizar_categoria:
        return categoria_schema.jsonify({'message': 'No se pudo actualizar la categoría'})

    data = request.get_json(force=True)
    cat_nom = data['cat_nom']
    cat_desp = data['cat_desp']

    actualizar_categoria.cat_nom = cat_nom
    actualizar_categoria.cat_desp = cat_desp

    db.session.commit()
    return categoria_schema.jsonify(actualizar_categoria)

# DELETE


@app.route('/Categoria/<id>', methods=['DELETE'])
def delete_categoria(id):
    eliminar_categoria = Categoria.query.get(id)
    db.session.delete(eliminar_categoria)
    db.session.commit()
    return categoria_schema.jsonify(eliminar_categoria)

# Mensaje de bienvenida


@app.route('/', methods=['GET'])
def index():
    return jsonify({'Mensaje': 'Bienvenido'})


# Correr el programa
if __name__ == '__main__':
    app.run(debug=True)
