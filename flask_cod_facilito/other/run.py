from flask import Flask

app = Flask(__name__)


@app.route('/run')
def index():
    return "Hola run.py"
