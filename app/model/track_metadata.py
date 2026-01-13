from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TrackMetadata(Base):
    __tablename__="track_metadata"

    id = Column(Integer, primary_key=True)
    artist = Column(String, nullable=False)
    album = Column(String, nullable=False)
    genre = Column(String, nullable=True)
    release_date = Column(DateTime(timezone=True))

    