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
    """
    Clase para leer con mutagen metadatos de un archivo de audio.
    TODO: ampliar aliases de los posibles tags a leer con mutagen.
    """
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
        En base a un AudioFile de mutagen extrae datos de un tag según
        sus posibles alias.

        Args:
            - audio (AudioFile): Objeto File de mutagen leído del fichero de audio a procesar
            - aliases (list): lista de posibles representaciones de un tag
        Return:
            - Valor como string del tag leído
        """
        for key in aliases:
            if audio.tags is None:
                continue
            value = audio.tags.get(key)
            if value:
                val = value[0] if isinstance(value, list) else value
                if hasattr(val, "text"):
                    val = val.text[0] if val.text else None
                return str(val)
        return None
    
    def analyze(self, file_path: str) -> AudioMetadata:
        """
        Dada una ruta a un archivo de audio, lo procesa con mutagen
        y guarda la información en la dataclass AudioMetadata.
        
        Args:
            - file_path (str): Ruta completa al archivo de audio.
        Return:
            - AudioMetadata: dataclass con los metadatos leídos.
        """
        audio = AudioFile(file_path)
        if not audio:
            return AudioMetadata()
        bpm_value = self.read_tag(audio, self.aliases["bpm"])
        try:
            bpm = float(bpm_value) if bpm_value else 0
        except (ValueError, TypeError):
            bpm = 0
        return AudioMetadata(
            title=self.read_tag(audio, self.aliases["title"]),
            artist=self.read_tag(audio, self.aliases["artist"]),
            album=self.read_tag(audio, self.aliases["album"]),
            duration=getattr(audio.info, "length", None),
            bpm=bpm,
            key=self.read_tag(audio, self.aliases["key"]),
        )

    