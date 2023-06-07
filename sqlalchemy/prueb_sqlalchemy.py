from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username = 'keynerrex'
password = 'keynerdel2015'
host = 'localhost'
port = 3307
database = 'sqlalchemy'

connection = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(connection)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'Usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    apellido = Column(String(255))


Base.metadata.create_all(engine)

if __name__ == '__main__':
    usuario = Usuario()
    usuario.nombre = 'keyner'
    usuario.apellido = 'oliveros'

    session.add(usuario)
    session.commit()

usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(usuario.nombre, usuario.apellido)

usuarios_filtrados = session.query(Usuario).filter(
    Usuario.nombre == 'keyner').first()
print(usuarios_filtrados.nombre)
