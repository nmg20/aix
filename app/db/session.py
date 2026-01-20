import os
from sqlalchemy import create_engine # type: ignore
from sqlalchemy.engine import URL # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from .base_class import Base

SQLALCHEMY_DATABASE_URL = (
    "mysql+pymysql://aixmin:aix@127.0.0.1:3306/aix"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()