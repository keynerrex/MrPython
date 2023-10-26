# comments.py
from flask import Blueprint, session, redirect, url_for, render_template, request, jsonify
from models.general import db, User, Comment
from forms.web_form import ComentarForm
from utils.decorators.decorators import login_required
import locale

comments_routes = Blueprint('comments', __name__)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


@comments_routes.route('/escribir-comentario', methods=['GET', 'POST'])
@login_required
def comment_to_form():
    title = "Escribir comentario"
    username = session.get('username')

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
def response_web_form():
    username = request.args.get('username')
    email = request.args.get('email')
    comment = request.args.get('comment')

    return render_template('response_web_form.html',
                           title="Datos Recibidos",
                           username=username,
                           email=email,
                           comment=comment)


@comments_routes.route('/mis-comentarios', methods=['GET', 'POST'])
@login_required
def my_comments():
    title = 'Mis Comentarios'
    my_comments_per_page = 5
    page = request.args.get('page', 1, type=int)

    username = session['username']
    current_user = User.query.filter_by(
        username=username).first()

    comments = Comment.query.with_entities(
        Comment.username,
        Comment.comment,
        Comment.create_date
    ).filter_by(username=current_user.username).paginate(
        page=page, per_page=my_comments_per_page)

    formatted_comments = []
    for comment in comments.items:
        formatted_date = comment.create_date.strftime("%A %d De %B Del %Y")
        formatted_comments.append(formatted_date.encode(
            'latin-1').decode('utf-8').capitalize())

    return render_template('my-comments.html',
                           title=title,
                           my_comments=comments,
                           formatted_comments=formatted_comments)


@comments_routes.route('/comentarios-usuarios2', methods=['GET'])
def show_comments():
    title = 'Comentarios de usuarios'
    users_per_page = 5
    page = request.args.get('page', 1, type=int)

    comments = Comment.query.with_entities(
        Comment.username,
        Comment.comment,
        Comment.create_date).paginate(
        page=page, per_page=users_per_page)

    total_pages = comments.pages

    formatted_usr_comments = []
    for comment_user in comments.items:
        formatted_date = comment_user.create_date.strftime(
            "%A %d De %B Del %Y")

        formatted_usr_comments.append(
            formatted_date.encode('latin-1').decode('utf-8').capitalize())

    return render_template('comentarios-usuarios.html',
                           title=title,
                           comments=comments,
                           formatted_usr_comments=formatted_usr_comments,
                           total_pages=total_pages)


@comments_routes.route('/comentarios', methods=['GET'])
def comentarios():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    comments = Comment.query.with_entities(
        Comment.username, Comment.comment, Comment.create_date).paginate(
        page=page, per_page=per_page, error_out=False)

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
def mostrar_comentarios():
    return render_template('comentarios.html', title='Comentarios de usuarios')
