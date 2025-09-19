from pydantic import BaseModel
from typing import List, Optional

class DownloadRequest(BaseModel):
    urls: List[str]

class Song(BaseModel):
    title: str
    url: str
    artist: Optional[str] = None
    album: Optional[str] = None

class PaginatedSongs(BaseModel):
    page: int
    size: int
    total: int
    songs: List[Song]