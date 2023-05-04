from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Retornamos al servidor"

# app.run(debug=True)