from dataclasses import dataclass
from mutagen import File as AudioFile  # type: ignore
from typing import List, Dict

@dataclass
class AudioMetadata:
    title: str | None = None
    artist: str | None = None
    album: str | None = None
    duration: float | None = None
    bpm: float | None = None
    key: str | None = None

class AudioAnalyzer:
    def __init__(self):
        self.aliases = {
            "title": ["TIT1", "TIT2", "title", "INAM"],
            "artist": ["TPE1", "TPE2", "artist", "albumartist", "IART"],
            "album": ["TALB", "album", "IRPD"],
            "bpm": ["TBPM", "bpm"],
            "key": ["TKEY", "initialkey"]
        }

    def read_tag(self, audio: AudioFile, aliases: list) -> str | None:
        """
        """
        for key in aliases:
            if audio.tags is None:
                continue
            value = audio.tags.get(key)
            if value:
                return value[0] if isinstance(value, list) else value
        return None
    
    def analyze(self, file_path: str) -> AudioMetadata:
        """
        """
        audio = AudioFile(file_path)
        if not audio:
            return AudioMetadata()
        
        return AudioMetadata(
            title=self.read_tag(audio, self.aliases["title"]),
            artist=self.read_tag(audio, self.aliases["artis"]),
            album=self.read_tag(audio, self.aliases["album"]),
            duration=getattr(audio.info, "length", None),
            bpm=float(self.read_tag(audio, self.aliases["bpm"]) or 0),
            key=self.read_tag(audio, self.aliases["key"]),
        )
    