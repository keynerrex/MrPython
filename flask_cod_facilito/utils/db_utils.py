from typing import Optional
from typing import TypeVar, Type
from models import db, Support, User


def get_data_table(model_class: type, table: Optional[str] = None, id: int = None) -> type:
    """
    Obtiene los datos de una tabla específica y un ID dado.

    ## Parámetros
    - `model_class` (SQLAlchemy Model): Clase del modelo de la tabla.
    - `table` (str, opcional): Nombre de la tabla. Si no se proporciona, se utilizará el nombre de la clase del modelo.
    - `id` (int, opcional): ID del registro a buscar. Si no se proporciona, se devolverá toda la información de la tabla.

    ## Retorna
    - `SQLAlchemy Model`: Registro encontrado.
    """
    if table is None:
        table = model_class.__tablename__

    if id is None:
        return model_class.query.all()
    else:
        return model_class.query.get(id)
