# comments.py
from flask import (Blueprint, session, redirect, url_for,
                   render_template, request, jsonify)
from models.general import (db, User, Comment)
from forms.web_form import ComentarForm
from utils.decorators.decorators import login_required
import locale

comments_routes = Blueprint('comments', __name__)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


@comments_routes.route('/escribir-comentario', methods=['GET', 'POST'])
@login_required
def comment_to_form():
    title = "Escribir comentario"
    username = session.get('username', 'NA')

    current_user = User.query.filter_by(username=username).first()
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


@comments_routes.route('/response_web_form', methods=['GET'])
@login_required
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


@comments_routes.route('/my-comments', methods=['GET'])
@login_required
def my_comments_():
    page = request.args.get('page', 1, type=int)

    username = session.get('username')

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


@comments_routes.route('/mis-comentarios', methods=['GET'])
@login_required
def show_my_comments():
    return render_template('/my-comments.html', title='Mis comentarios')


@comments_routes.route('/comentarios', methods=['GET'])
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


@comments_routes.route('/comentarios-usuarios', methods=['GET'])
def show_comments():
    return render_template('comments-users.html', title='Comentarios de usuarios')
