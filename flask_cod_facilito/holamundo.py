from flask import Flask

app = Flask(__name__)


@app.route('/holamundo')
def index():
    return "Retornamos al servidor"
