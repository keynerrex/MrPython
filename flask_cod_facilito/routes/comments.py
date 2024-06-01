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

    username = get_session_username()
    my_comments = Comment.query.with_entities(
        Comment.comment, Comment.create_date
    ).filter_by(username=username)

    comments_data = []
    for comment in my_comments:
        comments_data.append({
            'comment': comment.comment,
            'create_date': comment.create_date.strftime(
                "%d de %B del %Y")
        })
    return jsonify({
        'comments': comments_data
    })


@comments_routes.route(f'{path_url}mis-comentarios', methods=['GET'])
@role_required('Administrador', 'Soporte', 'Practicante', 'Usuario')
def show_my_comments():
    return render_template('/my-comments.html', title='Mis comentarios')


@comments_routes.route(f'{path_url}comentarios', methods=['GET'])
def comments():
    comments = Comment.query.with_entities(
        Comment.username, Comment.comment, Comment.create_date).all()

    # Procesa los comentarios y devuelve una respuesta JSON
    comments_data = []
    for comment in comments:
        comments_data.append({
            'username': comment.username,
            'comment': comment.comment,
            'create_date': comment.create_date.strftime(
                "%d de %B del %Y")
        })

    return jsonify({
        'comments': comments_data,
    })


@comments_routes.route(f'{path_url}comentarios-usuarios', methods=['GET'])
def show_comments():
    return render_template('comments-users.html', title='Comentarios de usuarios')


@comments_routes.route(f'{path_url}comentarios/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment:
        return jsonify({
            "commentID": comment.id,
            "comment": comment.comment,
            "create_date": comment.create_date.strftime(
                "%d de %B del %Y")
        })

    else:
        return jsonify({'error': 'Comment not found'}), 404


@comments_routes.route(f'{path_url}comentarios/<int:comment_id>', methods=['POST'])
def update_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        return jsonify({'error': 'Comentario not found'}), 404
    try:
        data = request.json

        if 'comment' in data:
            comment.comment = data['comment']

        if comment.comment == '':  # Por ejemplo, si el comment es 0
            raise ValueError("El comentario no puede estar vacío")
        
        db.session.commit()
        return jsonify({'message': 'El comentario ha sido actualizado'}), 200
    except Exception as e:
        return jsonify({'message': f'Ha ocurrido un error: {e}'}), 500
