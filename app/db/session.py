import os
from sqlalchemy import create_engine # type: ignore
from sqlalchemy.engine import URL # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

# SQLALCHEMY_DATABASE_URL = URL.create(
#     drivername="mysql+pymysql",
#     username=os.getenv("MYSQL_USER", "aix"),
#     password=os.getenv("MYSQL_PASSWORD", "aix"),
#     host=os.getenv("MYSQL_HOST", "127.0.0.1"),
#     database=os.getenv("MYSQL_DATABASE", "aix"),
#     port=int(os.getenv("MYSQL_PORT", 3306)),
# )

# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://aix:aix@127.0.0.1:3306/aix"

SQLALCHEMY_DATABASE_URL = (
    "mysql+pymysql://aix:aix@db:3306/aix"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()