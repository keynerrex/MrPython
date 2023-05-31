from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime

engine = create_engine(
    'mysql://keynerrex:keynerdel2015@localhost:3307/sqlalchemy')
Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    usuario = Column(String(20), nullable=False)
    creado = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.usuario


Session = sessionmaker(engine)
session = Session()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    usr = 'keynerrex'

    usuario = User(usuario=usr)
    session.add(usuario)
    session.commit()

    # Maneras de consultar
    consulta = session.query(User).filter_by(usuario='keynerrex').first()
    consulta2 = session.query(User).get(1)
    consulta3 = session.query(User).all()

    consulta4 = session.query(User).filter(
        User.usuario == 'keynerrex').with_entities(
            User.id, User.usuario, User.creado).first()

    consulta5 = session.query(User).with_entities(User.id, User.usuario).all()
    for dato in consulta5:
        print(dato)
