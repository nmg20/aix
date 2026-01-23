from pydantic import BaseModel
from app.schema.track import TrackRead

class PlaylistTrackBase(BaseModel):
    playlist_id: int
    track_id: int
    position: int | None = None

class PlaylistTrackCreate(PlaylistTrackBase):
    pass

class PlaylistTrackUpdate(PlaylistTrackBase):
    pass

class PlaylistTrackRead(PlaylistTrackBase):
    id: int
    track: TrackRead

    class Config:
        from_attributes = True