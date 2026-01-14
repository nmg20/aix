from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AudioFeature(Base):
    __tablename__="track_metadata"

    id = Column(Integer, primary_key=True)
    bpm = Column(Float, nullable=False)
    key = Column(String, nullable=False)
