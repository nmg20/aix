from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hashed_password = Column(String, nullable=True)
    is_superuser = Column(Boolean, default=False)

    # playlists = relationship("Playlist")