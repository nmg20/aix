from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class TrackSource(Base):
    __tablename__="track_sources"

    id = Column(Integer, primary_key=True)
    track_id = Column(Integer, ForeignKey("tracks.id"))
    provider = Column(String, nullable=False)
    path = Column(String, nullable=False)
    format = Column(String, nullable=True)
    bitrate = Column(Integer, nullable=True)

    created_at = Column(DateTime(timezone=True), 
        server_default=func.now())
    updated_at = Column(DateTime(timezone=True), 
        server_default=func.now(), onupdate=func.now())
    
    track = relationship("Track", back_populates="sources")
