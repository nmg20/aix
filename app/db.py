from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./aix.db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)