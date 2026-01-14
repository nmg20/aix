from app.model.track import Track
from app.schemas.track import TrackCreate, TrackInDB
from sqlalchemy.orm import Session
from typing import List, Optional

def create_track(db: Session, track: TrackCreate) -> Track:
    track_data : dict = track.model_dump()
    track_orm : Track = Track(**track_data)
    try:
        db.add(track_orm)
        db.commit()
        db.refresh(track_orm)
    except Exception:
        db.rollback()
        raise
    return track_orm

def get_track_by_id(db: Session, id: int) -> Optional[Track]:
    return db.query(Track).filter(Track.id == id).first()

def get_all_tracks(db: Session) -> List[Track]:
    return db.query(Track).all()

def get_track_by_title(db: Session, title: str) -> Optional[Track]:
    return db.query(Track).filter(Track.title == title).first()