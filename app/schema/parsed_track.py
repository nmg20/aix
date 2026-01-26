from typing import List
from pydantic import BaseModel

class ParsedTrackMetadata(BaseModel):
    artist: str | None = None
    album: str | None = None
    genre: str | None = None

class ParsedAudioFeature(BaseModel):
    bpm: float | None = None
    key: str | None = None

class ParsedTrack(BaseModel):
    title: str
    duration: float | None = None
    
    source: str
    path: str

    artist: str | None = None
    album: str | None = None
    genre: str | None = None

    bpm: float | None = None
    key: str | None = None

    # track_metadata: ParsedTrackMetadata | None = None
    # audio_features: ParsedAudioFeature | None = None