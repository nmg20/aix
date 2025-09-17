from yt_dlp import YoutubeDL # type: ignore
from urllib.parse import urlparse, parse_qs
from typing import List, Dict, Any
from app.models import Song

ydl_opts = {
    "extract_flat": True,
    "quiet": True,
    "force_generic_extractor": True,
    "ignoreerrors": True
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
    with YoutubeDL(ydl_opts) as ydl:
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

def download_songs(urls: List[str], output_dir="."):
    """
    Descarga canciones de YouTube.
    """
    opts = ydl_opts.copy()
    # opts.update({"outtmpl": f"{output_dir}/%(title)s.%(ext)s"})
    with YoutubeDL(opts) as ydl:
        ydl.download(urls)