from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class TrackMetadata(Base):
    __tablename__="track_metadata"

    id = Column(Integer, primary_key=True)
    artist = Column(String, nullable=False)
    album = Column(String, nullable=False)
    genre = Column(String, nullable=True)
    release_date = Column(DateTime(timezone=True))

    # track_id = Column(Integer, ForeignKey("tracks.id"))
    # track = relationship("Track")