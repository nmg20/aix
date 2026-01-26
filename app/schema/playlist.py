from app.schema.playlist_track import PlaylistTrackRead
from app.schema.parsed_track import ParsedTrack
from pydantic import BaseModel
from typing import List
import datetime

class PlaylistBase(BaseModel):
    name: str | None = None
    description: str | None = None
    provider: str
    path: str

class PlaylistCreate(PlaylistBase):
    author: str

class PlaylistUpdate(PlaylistBase):
    pass

class PlaylistParse(PlaylistBase):
    pass

class PlaylistParseResult(PlaylistBase):
    tracks: List[ParsedTrack]

class PlaylistRead(PlaylistBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    playlist_tracks: List[PlaylistTrackRead] = []

    class Config:
        from_attributes = True