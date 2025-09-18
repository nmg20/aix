from yt_dlp import YoutubeDL # type: ignore
from urllib.parse import urlparse, parse_qs
from typing import List, Dict, Any
from app.models import Song
from pathlib import Path
Path("./downloads").mkdir(exist_ok=True)

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


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    list_id = query.get("list")
    if list_id:
        return f"https://www.youtube.com/playlist?list={list_id[0]}"
    return url

def parse_playlist(url: str) -> List[Song]:
    """
    Analiza la playlist de YouTube y devuelve una lista de Songs.
    """
    with YoutubeDL(ydl_opts) as ydl: # type: ignore
        info = ydl.extract_info(normalize_url(url), download=False)
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

def download_songs(urls: list[str], output_dir="./downloads"):
    """
    Descarga canciones de YouTube.
    """
    print("Descargando canciones a:", output_dir)
    with YoutubeDL(ydl_opts_download) as ydl: # type: ignore
        ydl.download(urls)
    print("Descarga completada")