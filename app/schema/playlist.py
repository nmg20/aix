from app.schema.playlist_track import PlaylistTrackRead
from pydantic import BaseModel
from typing import List
import datetime

class PlaylistBase(BaseModel):
    name: str
    description: str | None = None
    provider: str

class PlaylistCreate(PlaylistBase):
    author: str
    path: str

class PlaylistRead(PlaylistBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    playlist_tracks: List[PlaylistTrackRead] = []

    class Config:
        from_attributes = True