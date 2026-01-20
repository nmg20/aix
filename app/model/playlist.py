from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Playlist(Base):
    __tablename__="playlists"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=False)
    author = Column(String(255), nullable=False)
    path = Column(String(255), nullable=False)

    created_at = Column(DateTime(timezone=True), 
        server_default=func.now())
    updated_at = Column(DateTime(timezone=True), 
        server_default=func.now(), onupdate=func.now())

    playlist_tracks = relationship("PlaylistTrack",
        back_populates="playlist",
        cascade="all, delete-orphan")