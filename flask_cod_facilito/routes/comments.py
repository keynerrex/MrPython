# comments.py
from flask import (Blueprint, session, redirect, url_for,
                   render_template, request, jsonify)
from models import (db, User, Comment)
from forms.web_form import ComentarForm
from utils.decorators.decorators import login_required, role_required, get_session_username, get_user_by_username
import locale

comments_routes = Blueprint('comments', __name__)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

path_url = '/comentarios/'

@comments_routes.route(f'{path_url}comentarios_new')
def comentarios():
    return render_template('comentarios.html')


@comments_routes.route(f'{path_url}comentarios_json')
def comentarios_json():
    current_user = get_session_username()
    print(current_user)
    comentarios = Comment.query.with_entities(
        Comment.id,
        Comment.comment,
        Comment.create_date
    ).filter_by(username=current_user).all()
    comments = []
    for comment in comentarios:
        comments.append({
            "id": comment.id,
            "comment": comment.comment,
            "create_date": comment.create_date.strftime('%d de %B del %Y')
        })
    return jsonify({
        "ResponseCode": "200 OK",
        "CodeResponse": 200,
        "comments": comments
    }), 200




@comments_routes.route(f'{path_url}escribir-comentario', methods=['GET', 'POST'])
@role_required('Administrador', 'Soporte', 'Practicante', 'Usuario')
def comment_to_form():
    title = "Escribir comentario"
    username = get_session_username()

    current_user = get_user_by_username(username)
    email = current_user.email if current_user else None

    comment_form = ComentarForm(request.form)

    if request.method == 'POST' and comment_form.validate():
        comment = Comment(
            username=username,
            comment=comment_form.comment.data)

        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('comments.response_web_form',
                                username=username,
                                email=email,
                                comment=comment_form.comment.data))

    else:
        return render_template('comment_user.html',
                               title=title,
                               form=comment_form,
                               username=username,
                               email=email)


@comments_routes.route(f'{path_url}response_web_form', methods=['GET'])
@role_required('Administrador', 'Soporte', 'Practicante', 'Usuario')
def response_web_form():
    if request.method == 'GET':
        username = request.args.get(
            'username', 'No se ha resgitrado un usuario')
        email = request.args.get('email', 'No se ha registrado un correo')
        comment = request.args.get(
            'comment', 'No se ha registrado ningún comentario')

    return render_template('response_web_form.html',
                           title="Datos Recibidos",
                           username=username,
                           email=email,
                           comment=comment)


@comments_routes.route(f'{path_url}my-comments', methods=['GET'])
@role_required('Administrador', 'Soporte', 'Practicante', 'Usuario')
def my_comments_():
    page = request.args.get('page', 1, type=int)

    username = get_session_username()

    my_comments = Comment.query.with_entities(
        Comment.comment, Comment.create_date
    ).filter_by(username=username).paginate(
        page=page, per_page=5, error_out=True)

    comments_data = []
    for comment in my_comments.items:
        comments_data.append({
            'comment': comment.comment,
            'create_date': comment.create_date.strftime(
                "%d de %B del %Y")
        })
    return jsonify({
        'comments': comments_data,
        'total_pages': my_comments.pages
    })


@comments_routes.route(f'{path_url}mis-comentarios', methods=['GET'])
@role_required('Administrador', 'Soporte', 'Practicante', 'Usuario')
def show_my_comments():
    return render_template('/my-comments.html', title='Mis comentarios')


@comments_routes.route(f'{path_url}comentarios', methods=['GET'])
def comments():
    page = request.args.get('page', 1, type=int)

    comments = Comment.query.with_entities(
        Comment.username, Comment.comment, Comment.create_date).paginate(
        page=page, per_page=5, error_out=False)

    # Procesa los comentarios y devuelve una respuesta JSON
    comments_data = []
    for comment in comments.items:
        comments_data.append({
            'username': comment.username,
            'comment': comment.comment,
            'create_date': comment.create_date.strftime(
                "%d de %B del %Y")
        })

    return jsonify({
        'comments': comments_data,
        'total_pages': comments.pages
    })


@comments_routes.route(f'{path_url}comentarios-usuarios', methods=['GET'])
def show_comments():
    return render_template('comments-users.html', title='Comentarios de usuarios')
