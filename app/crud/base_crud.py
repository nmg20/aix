from typing import TypeVar, Type, Optional, List, Generic
from pydantic import BaseModel
from sqlalchemy.orm import Session, DeclarativeBase

ORMModel = TypeVar("ORMModel", bound=DeclarativeBase)

class CrudRepository(Generic[ORMModel]):
    """
    Interfaz base para las operaciones CRUD.
    """

    def __init__(self, model: Type[ORMModel]) -> None:
        """
        Inicializa el repositorio CRUD.
        
        Args:
            - model (Type[ORMModel]): El modelo ORM usado para las operaciones CRUD.
        """
        self._model = model
        self._name = model.__name__
    
    def get_one(self, db: Session, *args, **kwargs) -> ORMModel | None:
        """
        Obtener un objeto de la base de datos.
        
        Args:
            - db (Session): Sesión de la base de datos.
            - *args: Número de argumentos variable para filtrar.
            - **kwargs: Número variable de argumentos de clave-valor para filtrar.
        
        Return:
            - ORMModel: Objeto obtenido si se encuentra.
        """
        return db.query(self._model).filter(*args).filter_by(**kwargs).first()

    def get_many(self, db: Session, *args, skip: int = 0, limit: int = 100, **kwargs) -> List[ORMModel]:
        """
        Obtener varios items de la base de datos.
        
        Args:
            - db (Session): Sesión de la base de datos.
            - *args: Número de argumentos variable.
                db.query(Class).filter(Class.name == 'name', Class.id > 3)
            - skip (int, optional): Items que saltarse.
            - limit (int, optional): Número máximo de items que devolver.
            - **kwargs: Número variable de argumentos de clave-valor.
                db.query(Class).filter_by()
        
        Return:
            - List[ORMModel]: Lista de items obtenidos.
        """
        return db.query(self._model).filter(*args).filter_by(**kwargs).offset(skip).limit(limit).all()

    def create(self, db: Session, schema: BaseModel):
        """
        Crea un objeto en la base de datos.

        Args:
            - db (Session): Sesión de la base de datos.
            - schema (BaseModel): Datos para crear el objeto (modelo de Pydantic).
        
        Return:
            - ORMModel: El nuevo objeto creado en la base de datos.
        """
        item_data = schema.model_dump()
        db_item = self._model(**item_data)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    def update(self, db: Session, item_id: int, schema: BaseModel) -> ORMModel | None:
        """
        Actualiza un objeto en la base de datos.

        Args:
            - db (Session): Sesión de la base de datos.
            - db_item (ORMModel): Objeto en la base de datos a actualizar.
            - schema (BaseModel): Datos del objeto que actualizar.
        
        Return:
            - ORMModel: Objeto de la base de datos actualizado.
        """
        db_item = db.get(self._model, item_id)
        if db_item is None:
            return None
        update_item_data = schema.model_dump(exclude_unset=True)
        for field, data in update_item_data.items():
            setattr(db_item, field, data)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    def delete(self, db: Session, item_id: int) -> ORMModel | None:
        """
        Borra un objeto de la base de datos.

        Args:
            - db (Session): Sesión de la base de datos.
            - db_item (ORMModel): Objeto de la base de datos que borrar.
        
        Return:
            ORMModel: Objeto borrado de la base de datos.
        """
        db_item = db.get(self._model, item_id)
        if db_item is None:
            return None
        db.delete(db_item)
        db.commit()
        return db_item