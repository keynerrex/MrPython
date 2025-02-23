# comments.py
from flask import (Blueprint, redirect, url_for,
                   render_template, request, jsonify)
from models import (db, User, Comment)
from utils.decorators import role_required, get_session_username, get_user_by_username
from utils.db_utils import send_mail
from config.mail import mail, Message, MailConfig
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
    ).filter_by(username=current_user).where(Comment.status == 1).all()

    comments = []
    for comment in comentarios:
        comment_dict = {
            "id": comment.id,
            "comment": comment.comment
        }

        if comment.create_date:
            comment_dict['create_date'] = comment.create_date.strftime(
                '%d de %B del %Y')
        else:
            comment_dict['create_date'] = "Sin fecha"

        comments.append(comment_dict)

    return jsonify({
        "ResponseCode": "200 OK",
        "CodeResponse": 200,
        "comments": comments
    }), 200


@comments_routes.route(f'{path_url}escribir-comentario', methods=['GET', 'POST'])
@role_required('Administrador', 'Soporte', 'Practicante', 'Usuario')
def comment_to_form():
    if request.method == 'POST':
        username = get_session_username()
        user = get_user_by_username(username)
        if user:
            try:
                comment = request.form.get('comment')
                if not comment:
                    return jsonify({'status': 'error', 'message': 'El comentario no puede estar vacio'}), 400

                comment = Comment(username=username, comment=comment)
                db.session.add(comment)
                db.session.commit()
                return jsonify({'status': 'success', 'message': 'Comentario hecho'})

            except KeyError:
                return jsonify({'status': 'error', 'message': 'Error de llave no encontrada'}), 400
            except ValueError:
                return jsonify({'status': 'error', 'message': 'Error de valores'}), 400
            except Exception as e:
                return jsonify({'status': 'error', 'message': 'Se ha presentado un error'}), 500
            finally:
                db.session.rollback()
                db.session.close()

    return render_template('add_comment.html')


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
        Comment.username, Comment.comment, Comment.create_date).filter(Comment.status == 1).all()

    comments_data = []
    for comment in comments:
        comment_dict = {
            'username': str(comment.username) if comment.username else 'Anónimo',
            'comment': comment.comment
        }
        # Verificar si hay fecha correcta, si no lo es o es null se devolvera sin fecha
        if comment.create_date:
            comment_dict['create_date'] = comment.create_date.strftime(
                '%d de %B del %Y')
        else:
            comment_dict['create_date'] = 'Sin fecha'

        comments_data.append(comment_dict)

    return jsonify({
        'comments': comments_data,
    })


@comments_routes.route(f'{path_url}comentarios-usuarios', methods=['GET'])
def show_comments():
    return render_template('comments-users.html', title='Comentarios de usuarios')


@comments_routes.route(f'{path_url}comentarios/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comment.query.get(comment_id)
    comments_data = []
    if comment:
        comment_dict = {
            "commentID": comment.id,
            "comment": comment.comment,
        }

        # Verificar si hay fecha correcta, si no lo es o es null se devolvera sin fecha
        if comment.create_date:
            comment_dict['create_date'] = comment.create_date.strftime(
                '%d de %B del %Y')
        else:
            comment_dict['create_date'] = 'Sin fecha'

        comments_data.append(comment_dict)
        return jsonify({
            'commentID': comment_dict['commentID'],
            'comment': comment_dict['comment'],
            'create_date': comment_dict['create_date']
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

        if comment.comment == '':
            raise ValueError("El comentario no puede estar vacio")

        db.session.commit()
        return jsonify({'success': 'El comentario ha sido actualizado'}), 200
    except Exception as e:
        return jsonify({'error': f'Ha ocurrido un error: {e}'}), 500


@comments_routes.route(f'{path_url}comentarios/<int:comment_id>', methods=['DELETE'])
def deleteComment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({'error': 'Comentario not found'}), 404
    try:
        email_user = User.query.with_entities(User.email).filter(
            User.username == comment.username).first()

        data = request.json
        if data and 'id' in data:
            comment.status = 0
        if email_user:
            camps = {
                'id_comment': comment.id,
                'comment': comment.comment
            }
            send_mail('Información de comentario borrado',
                      email_to=email_user, context=camps, html='notify_comment_delete.html')
        db.session.delete(comment)
        db.session.commit()

        return jsonify({'message': 'El comentario ha sido eliminado'}), 200
    except Exception as e:
        return jsonify({'message': f'Ha ocurrido un error: {e}'}), 500
