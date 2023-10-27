# comments.py
<<<<<<< HEAD
from flask import Blueprint, session, redirect, url_for, render_template, request
=======
from flask import Blueprint, session, redirect, url_for, render_template, request, jsonify
>>>>>>> parent of 618edb6 (MRP-21 cargando para todos los listados en las tablas)
from models.general import db, User, Comment
from forms.web_form import ComentarForm
import locale

comments_routes = Blueprint('comments', __name__)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


@comments_routes.route('/escribir-comentario', methods=['GET', 'POST'])
def comment_to_form():
    if 'username' not in session:
        return redirect(url_for('login'))

    title = "Escribir comentario"
<<<<<<< HEAD
    username = session['username']
=======
    username = session.get('username')
>>>>>>> parent of 618edb6 (MRP-21 cargando para todos los listados en las tablas)

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
<<<<<<< HEAD
def my_comments():
    if 'username' not in session:
        return redirect(url_for('home.login'))

=======
@login_required
def my_comments():
>>>>>>> parent of 618edb6 (MRP-21 cargando para todos los listados en las tablas)
    title = 'Mis Comentarios'
    my_comments_per_page = 5
    page = request.args.get('page', 1, type=int)

    username = session['username']
    current_user = User.query.filter_by(
        username=username).first()
<<<<<<< HEAD
=======

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
>>>>>>> parent of 618edb6 (MRP-21 cargando para todos los listados en las tablas)

    comments = Comment.query.with_entities(
        Comment.username,
        Comment.comment,
<<<<<<< HEAD
        Comment.create_date
    ).filter_by(username=current_user.username).paginate(
        page=page, per_page=my_comments_per_page)
=======
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
>>>>>>> parent of 618edb6 (MRP-21 cargando para todos los listados en las tablas)

    formatted_comments = []
    for comment in comments.items:
        formatted_date = comment.create_date.strftime("%A %d De %B Del %Y")
        formatted_comments.append(formatted_date.encode(
            'latin-1').decode('utf-8').capitalize())

    return render_template('my-comments.html',
                           title=title,
                           my_comments=comments,
                           formatted_comments=formatted_comments)


@comments_routes.route('/comentarios-usuarios', methods=['GET'])
<<<<<<< HEAD
def show_comments():
    title = 'Comentarios de usuarios'
    users_per_page = 5
    page = request.args.get('page', 1, type=int)

    comments = Comment.query.with_entities(Comment.username,
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
=======
def mostrar_comentarios():
    return render_template('comentarios.html', title='Comentarios de usuarios')
>>>>>>> parent of 618edb6 (MRP-21 cargando para todos los listados en las tablas)
