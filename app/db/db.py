from app.db.session import SessionLocal
from typing import Generator

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        raise(e)
    finally:
        db.close()