from flask import Flask, render_template

app = Flask(__name__)


@app.route('/macro')
def index():
    title = "Curso Flask -MACRO"
    return render_template('macro.html', title=title)


if __name__ == '__main__':
    app.run(port=8000, debug=True)

# No repite codigo -> Macro
