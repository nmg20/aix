from sqlalchemy import MetaData
from typing import Dict, Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

INDEX_NAMING_CONVENTION = {
    "ix": "ix_%(table_name)s_%(column_0_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=INDEX_NAMING_CONVENTION)

class_registry: Dict[str, Any] = {}

@as_declarative(class_registry=class_registry)
class Base:
    id: Any
    __name__: str
    __abstract__: bool = True
    metadata: MetaData = metadata