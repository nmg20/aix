from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Track(Base):
    __tablename__="tracks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=False)
    duration = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), 
        server_default=func.now())
    updated_at = Column(DateTime(timezone=True), 
        server_default=func.now(), onupdate=func.now())

    sources = relationship("TrackSource",
        back_populates="track", cascade="all")
    audio_features = relationship("AudioFeature",
        back_populates="track", cascade="all")
    metadata = relationship("TrackMetadata",
        back_populates="track", cascade="all")

    