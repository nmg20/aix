from datetime import datetime
from typing import Dict, Optional, List, Tuple
from urllib.parse import urlparse, parse_qs
from app.models import Song
from app.services.providers.youtube_provider import YoutubeProvider
import threading

PROVIDERS = {
    "youtube": YoutubeProvider()
}

class PlaylistService:
    """
    Servicio central con manejo de providers (YouTube, SoundCloud, etc.).
    """
    def __init__(self):
        self.cache: dict[tuple[str, str], list[Song]] = {}

    def _get_provider(self, url: str):
        for name, provider in PROVIDERS.items():
            if provider.supports(url):
                return name, provider
        raise ValueError(f"Soporte para la URL: {url} no disponible aún :(")

    def parse_playlist(self, 
        url: str,
        search: Optional[str] = None,
        # added_before: Optional[datetime] = None,
        # added_after: Optional[datetime] = None
        ) -> List[Song]:
        """
        Parsea la playlist, aplica filtros y devuelve la lista de canciones.
        """
        provider_name, provider = self._get_provider(url)
        key = (provider_name, url)

        if key not in self.cache:
            self.cache[key] = provider.parse(url)
        
        songs = self.cache[key]

        # Filtrar por nombre
        if search:
            songs = [
                song for song in songs
                if (search.lower() in song.title.lower())
            ]
        
        # TODO: filtrar por fechas

        return songs
    
    def get_page(self,
        songs: List[Song],
        page: int = 1,
        size: int = 30) -> Tuple[List[Song], int]:
        """
        Devuelve la lista de canciones paginada.
        """
        start = (page - 1) * size
        end = start + size
        return songs[start:end], len(songs)
    
    def download_songs(self,
        songs: List[Song],
        output_dir: str = "./downloads"):
        """
        Descarga la lista de canciones de forma concurrente.
        """
        def _download(song: Song):
            provider_name, provider = self._get_provider(song.url)
            provider.download([song], output_dir)
        
        threads = []
        for song in songs:
            t = threading.Thread(target=_download, args=(song,))
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()