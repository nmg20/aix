from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Track(Base):
    __tablename__="tracks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=False)

    audio_features = relationship("AudioFeature")
    metadata = relationship("TrackMetadata")

    