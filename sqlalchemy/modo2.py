from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, create_engine, text

engine = create_engine(
    'mysql://keynerrex:keynerdel2015@localhost:3307/sqlalchemy')
Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    usuario = Column(String(20), nullable=False)
    correo = Column(String(255))
    creado = Column(DateTime(), server_default=text('CURRENT_TIMESTAMP'))

    def __str__(self):
        return self.usuario

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):
        self.correo = correo


class Correo(Base):
    __tablename__ = 'Correos'
    id = Column(Integer, primary_key=True)
    correo = Column(String(255), nullable=False)

    def __str__(self):
        return self.correo


def consultas2():
    "SELECT * FROM users"

    query = session.query(User).all()
    for dato in query:
        print(dato.id, " - ", dato.usuario)


def filtros():
    "SELECT * FROM users WHERE id >= 1 AND usuario = 'usuario3"

    query = session.query(User).filter(
        User.id >= 1).filter(User.usuario == 'usuario3')

    for dato in query:
        print(dato.id, ' - ', dato.usuario, ' - ', dato.creado)


def filtros2():
    "SELECT id,correo FROM users WHERE id >= 1 AND usuario = 'usuario3'"

    query = session.query(User.id, User.correo).filter(
        User.id >= 1).filter(User.usuario == 'usuario3')

    for dato in query:
        print(dato.id, ' - ', dato.correo)


def filtros3():
    # Consultas Unicas( first(devuelve None),one(lanza excepcion) )
    """SELECT * FROM users WHERE id = 50 LIMIT 1"""
    user = session.query(User).filter(User.id == 50).first()

    if user is not None:
        print(user)
    else:
        print(f"No existe este usuario")


def actualizar():
    """SELECT * FROM users WHERE id = 50"""

    user = session.query(User).filter(User.id == 5).first()
    user.usuario = 'usernuevo50'
    user.set_correo('usernuevo5000@gmail.com')

    session.add(user)
    session.commit()
    print(user)


def actualizar2():
    # 2
    """UPDATE user SET usuario = 'usernuevo156',correo = 'emailnuevo156@gmail.com'
    WHERE (id = '51');"""

    session.query(User).filter(User.id == 156).update(
        {
            User.usuario: 'usernuevo157',
            User.correo: 'keyner@gmail.com'.lower()
        }
    )

    session.commit()
    print(session.query(User.usuario, User.correo).filter(User.id == 156).first())


def eliminar():
    """DELETE FROM user WHERE id = 156"""

    try:
        session.query(User).filter(User.id == 156).delete()
        session.commit()
        print(f"Se ha eliminado el registro")

    except Exception as err:
        print(f"Ocurrió un error al eliminar: {err}")

    finally:
        session.rollback()
        session.close()


Session = sessionmaker(engine)
session = Session()

__name__ = 'actualizar_1_2'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    usr = 'keynerrex'
    crr = 'keyner@gamil.com'

    try:
        """INSERT INTO users (username,correo)
        VALUES('usuario','example@gmail.com')"""

        user1 = User(usuario=usr, correo=crr)
        session.add(user1)
        session.commit()
        print(f"Inserccion correcta: {user1}")

    except Exception as err:
        session.rollback()
        print(f"Ha ocurrido un error: {err}")

    finally:
        session.close()

elif __name__ == 'consultas2':
    consultas2()

elif __name__ == 'filtros':
    filtros()

elif __name__ == 'filtros2':
    filtros2()

elif __name__ == 'filtros3':
    filtros3()

elif __name__ == 'actualizar_1_2':
    actualizar()

elif __name__ == 'eliminar':
    eliminar()
