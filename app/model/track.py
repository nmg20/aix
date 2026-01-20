from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Track(Base):
    __tablename__="tracks"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, unique=False)
    duration = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), 
        server_default=func.now())
    updated_at = Column(DateTime(timezone=True), 
        server_default=func.now(), onupdate=func.now())

    sources = relationship("TrackSource",
        back_populates="track", cascade="all, delete-orphan")
    # audio_features = relationship("AudioFeature",
    #     back_populates="track", cascade="all")
    # track_metadata = relationship("TrackMetadata",
    #     back_populates="track", cascade="all")

    playlist_tracks = relationship("PlaylistTrack",
        back_populates="track",
        cascade="all, delete-orphan")

    