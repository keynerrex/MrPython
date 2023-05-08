from flask import Flask

app = Flask(__name__)


@app.route('/run')
def index():
    return "Hola run.py"


# if __name__ == '__main__':
#     app.run(port=8000, debug=True)

