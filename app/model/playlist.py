from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Playlist(Base):
    __tablename__="playlists"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=False)
    path = Column(String, nullable=False)

    