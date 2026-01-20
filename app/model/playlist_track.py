from app.db.base_class import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class PlaylistTrack(Base):
    __tablename__="playlist_tracks"

    id = Column(Integer, primary_key=True)

    playlist_id = Column(Integer, 
        ForeignKey("playlists.id", ondelete="cascade"),
        nullable=False)
    track_id = Column(Integer,
        ForeignKey("tracks.id", ondelete="cascade"),
        nullable=False)
    
    created_at = Column(DateTime(timezone=True),
        server_default=func.now())
    
    playlist = relationship("Playlist", 
        back_populates="playlist_tracks")
    track = relationship("Track", 
        back_populates="playlist_tracks")
    
    __table_args__ = (
        UniqueConstraint("playlist_id", "track_id", name="uq_playlist_track"),
    )