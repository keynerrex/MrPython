import os
import subprocess
import time
from sqlalchemy.exc import IntegrityError
from models import db, User, Rol
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import ProductionConfig

service_name = "MySQL80"
engine = create_engine(ProductionConfig.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)


def start_mysql_service():
    try:
        subprocess.run(["net", "start", service_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al iniciar el servicio {service_name}: {e}")


def activate_user(username, statui):
    session = Session()

    try:
        user = session.query(User).filter_by(
            username=username, status=0).first()
        if user:
            user.status = 1
            session.commit()
            print(f"Usuario {username} activado correctamente.")

        else:
            print(f"El usuario {username} ya estaba activo o no existe.")

    except Exception as e:
        session.rollback()
        print(f"Error al activar usuario: {e}")

    finally:
        session.close()


def rol_user(username, rol):
    session = Session()
    try:
        user = session.query(User).filter_by(username=username).first()
        rol_user = session.query(Rol.rol).filter_by(id=rol).first()

        if user:
            user.rol_id = rol
            session.commit()
            print(
                f"El usuario {username} ha sido cambiado al rol {rol_user[0]}")
        else:
            print(
                f"El usuario {username} ya se encuentra con el mismo rol o no existe")

    except IntegrityError as e:
        session.rollback()
        print({'Error': 'Se ha intentado insertar un rol no existente'})

    except Exception as e:
        session.rollback()
        print(f"Ha ocurrido un error: {e}")

    finally:
        session.close()


if __name__ == "__main__":

    # start_mysql_service()
    # activate_user('keynerrex')
    rol_user('keynerrex', 1)
