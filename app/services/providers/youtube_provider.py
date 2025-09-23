from typing import List
from urllib.parse import urlparse, parse_qs
from app.models import Song
from app.services.providers.base import ProviderBase

ydl_opts = {
    "extract_flat": True,
    "quiet": True,
    "ignoreerrors": True
}

ydl_opts_download = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "quiet": False,
    "ignoreerrors": True,
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "320"
    }]
}

class YoutubeProvider(ProviderBase):
    name = "youtube"

    def supports(self, url: str) -> bool:
        """
        Comprobar si es una URL de YouTube.
        """
        parsed = urlparse(url)
        return "youtube.com" in parsed.netloc or "youtu.be" in parsed.netloc

    def _normalize_url(self, url: str) -> str:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        list_id = query.get("list")
        if list_id:
            return f"https://www.youtube.com/playlist?list={list_id[0]}"
        return url

    def parse(self, url: str) -> List[Song]:
        """
        Analizar la URL y devolver la lista de canciones
        """
        with YoutubeDL(ydl_opts) as ydl: # type: ignore
            info = ydl.extract_info(self._normalize_url(url), download=False)
            entries = info.get("entries", [])
            songs: List[Song] = []
            for e in entries:
                song = Song(
                    title=e.get("title", "Unknown title"),
                    url=e.get("url"),
                    artist=e.get("artist"),
                    album=e.get("album")
                )
                songs.append(song)
            return songs
    
    def download(self, songs: List[Song], output_dir: str):
        """
        Descarga la lista de canciones.
        Song -> url -> download(List)
        """
        urls = [song.url for song in songs if song.url]
        if not urls:
            print("No hay canciones disponibles para descargar :(")
            return
        
        opts = ydl_opts_download.copy()
        opts["outtmpl"] = f"{output_dir}/%(title)s.%(ext)s"

        print(f"Descargando {len(urls)} canciones a {output_dir}.")
        with YoutubeDL(ydl_opts_download) as ydl: # type: ignore
            ydl.download(urls)
        print("Descarga completada")
