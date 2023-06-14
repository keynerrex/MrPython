from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import (Column, Integer, String, DateTime,
                        create_engine, text, CheckConstraint,
                        ForeignKey, select, func, exists, select)

engine = create_engine(
    'mysql://keynerrex:keynerdel2015@localhost:3307/sqlalchemy')
Base = declarative_base()

Session = sessionmaker(engine)
session = Session()


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


class Padre(Base):
    __tablename__ = 'Padre'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), server_default='No tiene')
    apellido = Column(String(30), server_default='No tiene')
    edad = Column(Integer, server_default=text('0'))
    __table_args__ = (
        CheckConstraint('edad >= 0 AND edad <= 99', name='chk_edad_range'),
    )
    hijos = relationship("Hijo", back_populates="padre")
    creado = Column(DateTime(), server_default=text('CURRENT_TIMESTAMP'))


class Hijo(Base):
    __tablename__ = 'Hijo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), server_default='No tiene')
    apellido = Column(String(30), server_default='No tiene')
    padre_id = Column(Integer, ForeignKey('Padre.id'))
    creado = Column(DateTime(), server_default=text('CURRENT_TIMESTAMP'))
    padre = relationship("Padre", back_populates="hijos")


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
    """SELECT * FROM users WHERE id = 1011"""

    try:
        user = session.query(User).filter(User.id == 1011).first()
        user.usuario = 'usernuevo50'
        user.set_correo('usernuevo5000@gmail.com')

        session.add(user)
        session.commit()
        print(user)

    except Exception as e:
        print(f"Este usuario no existe, no se pudo actualizar")

    finally:
        session.rollback()
        session.close()


def actualizar2():
    # 2
    """UPDATE user SET usuario = 'usernuevo1501',correo = 'keyner1501@gmail.com'
    WHERE (id = '1501');"""

    try:
        session.query(User).filter(User.id == 1501).update(
            {
                User.usuario: 'usernuevo1501',
                User.correo: 'keyner1501@gmail.com'.lower()
            }
        )

        session.commit()
        print(session.query(User.id, User.usuario, User.correo).filter(
            User.id == 1501).first())

    except Exception as e:
        print("error: {e}")


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


def consulta_relacionada1():
    """SELECT h.id, h.nombre, h.apellido, CONCAT(p.nombre,' ',p.apellido) AS Padre 
    FROM hijo AS h
    INNER JOIN padre AS p
    ON h.padre_id = p.id;"""

    query = select([
        Hijo.id,
        Hijo.nombre,
        Hijo.apellido,
        func.concat(Padre.nombre, ' ', Padre.apellido).label('Padre')
    ]).join(Padre, Hijo.padre_id == Padre.id)

    print(query)


def consulta_relacionada2() -> list:
    """SELECT h.id, h.nombre, h.apellido,
    CONCAT(p.nombre,' ',p.apellido) AS Padre, h.creado
    FROM hijo AS h
    INNER JOIN padre AS p
    ON h.padre_id = p.id
    WHERE h.apellido = p.apellido;"""

    query = session.query(
        Hijo.id, Hijo.nombre, Hijo.apellido,
        func.concat(Padre.nombre, ' ', Padre.apellido), Hijo.creado).\
        join(Padre, Hijo.padre_id == Padre.id).filter(
            Hijo.apellido == Padre.apellido).all()

    resultados = []
    for hijo in query:
        resultados.append(
            (hijo[0], hijo[1], hijo[2], hijo[3], hijo[4]))

    return resultados


def consulta_relacionada3():
    """SELECT h.id, h.nombre, h.apellido, p.id
    FROM hijo AS h
    INNER JOIN padre AS p ON h.padre_id = p.id
    WHERE h.apellido = p.apellido
    AND h.padre_id = p.id
    AND (
      SELECT COUNT(*)
      FROM hijo
      WHERE apellido = h.apellido AND padre_id = h.padre_id
    ) >= 2;"""

    subquery = session.query(func.count()).filter(
        Hijo.apellido == Padre.apellido,
        Hijo.padre_id == Padre.id,
        Hijo.apellido.isnot(None)).group_by(
        Hijo.apellido, Hijo.padre_id).having(
        func.count() >= 2).subquery()

    query = session.query(
        Hijo.id, Hijo.nombre, Hijo.apellido, Padre.id).join(
        Padre, Hijo.padre_id == Padre.id).filter(
        Hijo.apellido == Padre.apellido,
        Hijo.padre_id == Padre.id,
        exists(subquery)).all()

    for resultado in query:
        print(resultado)


__name__ = 'consultas_relacionadas3'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    usr = 'keynerrex'
    crr = 'keyner@gmil.com'

    try:
        query = session.query(Hijo).with_entities(
            Hijo.id, Hijo.nombre, Hijo.apellido, Padre.nombre).all()
        print(query)

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
    actualizar2()

elif __name__ == 'eliminar':
    eliminar()

elif __name__ == 'consultas_relacionadas':
    resultados = consulta_relacionada2()
    for hijo in resultados:
        print(
            f"{hijo[0]} --- {hijo[1]} --- {hijo[2]} --- {hijo[3]} --- {hijo[4]}")

elif __name__ == 'consultas_relacionadas3':
    consulta_relacionada3()
