from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Playlist(Base):
    __tablename__="playlists"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=False)
    path = Column(String, nullable=False)

    tracks = relationship("Track")