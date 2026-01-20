from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class AudioFeature(Base):
    __tablename__="audio_features"

    id = Column(Integer, primary_key=True)
    bpm = Column(Float, nullable=False)
    key = Column(String, nullable=False)

    # track_id = Column(Integer, ForeignKey("tracks.id"))
    # track = relationship("Track")
