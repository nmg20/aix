from app.providers.base_provider import PlaylistProvider
from app.schema.playlist import PlaylistParseResult
from app.schema.parsed_track import ParsedTrack
from app.providers.metadata_reader import AudioMetadata, AudioAnalyzer
from typing import List
import os

class LocalProvider(PlaylistProvider):
    """
    Procesador de tracks en forma de archivos locales en carpetas.
    """
    def __init__(self):
        super().__init__("local")
        self.supported_formats = (".mp3",".wav",".flac")
        self.analyzer = AudioAnalyzer()

    def parse_playlist(self, path: str) -> PlaylistParseResult:
        """
        En base a la ruta de una carpeta devuelve los datos de los
        tracks en esa playlist.

        Args:
            - path (str): Ruta a la carpeta local
        Return:
            - PlaylistParseResult: Provider + path de la playlist 
                + lista de tracks procesados
        """
        print(f"[PROVIDER]Parsing playlist: {path}.\n")
        files = self.scan_folder(path)
        tracks: List[ParsedTrack] = []

        for file in files:
            tracks.append(self.read_metadata(file))
        
        return PlaylistParseResult(
            provider=self.name,
            path=path,
            tracks=tracks
        )

    def scan_folder(self, path: str) -> List[str]:
        """
        Devuelve los archivos en path que coincidan con los formatos
        de audio admitidos.

        Args:
            - path: Ruta a la carpeta
        Return:
            - Lista de paths de los archivos en la carpeta
        """
        if not os.path.isdir(path):
            raise ValueError(f"Path is not a directory: {path}")

        return [
            os.path.join(path, f)
            for f in os.listdir(path)
            if f.lower().endswith(self.supported_formats)
        ]
    
    def read_metadata(self, file_path: str) -> ParsedTrack:
        """
        Lee metadatos de un track con mutagen teniendo en cuenta 
        el formato del archivo.

        Args:
            - file_path (str): Ruta absolutaal archivo de audio
        Return:
            - ParsedTrack: Clase con metadatos rellenados después de 
            parsear un track
        """
        print(f"\tReading {file_path} metadata.\n")
        metadata: AudioMetadata = self.analyzer.analyze(file_path)
        return ParsedTrack(
            title=metadata.title if metadata.title else file_path,
            duration=metadata.duration,
            source="local",
            path=file_path,
            artist=metadata.artist,
            album=metadata.album,
            bpm=metadata.bpm,
            key=metadata.key,            
        )
    
    def download_playlist(self, tracks: List[ParsedTrack]) -> None:
        """
        No soportada porque los tracks de esta playlist ya están descargados.
        """
        pass
