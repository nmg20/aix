from app.schema.parsed_track import ParsedTrack
from app.schema.playlist import PlaylistParseResult
from abc import ABC, abstractmethod
from typing import List

class PlaylistProvider(ABC):
    """
    Clase básica relacionada con el manejo de tracks de una playlist.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def parse_playlist(self, path: str) -> PlaylistParseResult:
        pass

    @abstractmethod
    def download_playlist(self, tracks: List[ParsedTrack]) -> None:
        pass