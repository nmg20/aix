from app.model.track import Track
from app.model.track_source import TrackSource
from app.schema.track import TrackCreate, TrackUpdate
from app.schema.track_source import TrackSourceCreate
from app.crud.base_crud import CrudRepository
from sqlalchemy.orm import Session
from pydantic import BaseModel

class TrackCrud(CrudRepository):
    def __init__(self) -> None:
        super().__init__(Track)

    def create(self, db: Session, track: TrackCreate,
            ) -> Track:
        """
        """
        sources_data = track.sources or []

        created_track = Track(
            **track.model_dump(exclude={"sources"})
        )

        for source in sources_data:
            created_track.sources.append(
                TrackSource(**source.model_dump())
            )

        db.add(created_track)
        db.commit()
        db.refresh(created_track)
        return created_track
    
    def update(self, db: Session, track_id: int,
            track_data: TrackUpdate) -> Track | None:
        track = db.get(Track, track_id)
        if track is None:
            return None
        
        for field, data in track_data.model_dump(exclude_unset=True):
            setattr(track, field, data)
        
        db.add(track)
        db.commit()
        db.refresh(track)
        return track
        
track_crud = TrackCrud()