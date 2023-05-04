from flask import Flask, request, make_response, redirect
# Lugar del template
app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr
    # crear una cookie
    response = make_response(redirect('/hello'))
    # como se va llamar la cookie y lo que va llevar(ip)
    response. set_cookie('user_ip', user_ip)
    return response


# Mensaje de bienvenida
@app.route('/hello')
def hello():
    # ip
    user_ip = request.cookies.get('user_ip')

    return f"Su dirección IP es: {user_ip}"


# Correr
if __name__ == "__main__":
    app.run(port=5000, debug=True)
