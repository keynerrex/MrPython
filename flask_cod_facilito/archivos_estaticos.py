from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = "Curso Flask"
    return render_template('archivos_estaticos.html', title=title)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
