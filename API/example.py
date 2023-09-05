from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello_world():
    resp = {"Message": "Hola mundo"}
    return jsonify(resp)


@app.route('/edad/<int:age>', methods=['POST'])
def age(age):
    if age < 18:
        resp = {"Message": "Para entrar debes ser mayor de edad"}
        return jsonify(resp)

    elif age:
        resp = {"Message": "Edad confirmada, por favor siga"}
    return jsonify(resp)


@app.route('/nombre=<string:name>', methods=['POST'])
def name(name):
    resp = {"ResponseCode": "200",
            "data": [{"Name": name}]}
    return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True)
