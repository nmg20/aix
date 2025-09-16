import os
from pathlib import Path
from typing import List, Optional
from mutagen import File
from mutagen.flac import FLAC
from mutagen.wave import WAVE
from mutagen.mp3 import MP3
from mutagen.aiff import AIFF

from sqlmodel import Session, select
from ..db import get_session
from ..models import Playlist, Song, SongInfo, SongCreate, SongRead
from ..config import SUPPORTED_FORMATS, DEFAULT_PLAYLIST_PATH

TITLE_TAGS = ["title", "TIT2"]
ARTIST_TAGS = ["artist", "TPE1"]
ALBUM_TAGS = ["album", "IPRD"]
RELEASE_TAGS = ["date", "TDRC"]
BPM_TAGS = ["BPM", "TBPM", "bpm"]
KEY_TAGS = ["initialkey", "TKEY"]

def sync_playlist(path: Optional[str] = None, recursive: bool = True):
    """
    Leer de forma superficial las canciones en una carpeta.
    path : str = ruta a la carpeta a analizar (se toma la ruta por defecto si no se pasa)
    recusrive : bool = flag para analizar subcarpetas dentro de la carpeta especificada
    """

    folder_path = path or DEFAULT_PLAYLIST_PATH
    # if not folder_path.exists() or not folder_path.is_dir():
    #     return {"status": "error", "message": "La carpeta no existe"}

    # for file in folder_path.glob("*"):
    #     pass

def scan_track(song: Song):
    pass

def process_track(path: str):
    audio = File(path)
    if audio is None:
        raise ValueError(f"Formato no reconocido: {path}")
    
    tags = audio.tags

    return SongInfo(
        path = path,
        title = extract_title(tags),
        artist = extract_artist(tags),
        album = extract_album(tags),
        release = extract_release_date(tags),
        bpm = extract_bpm(tags),
        key = extract_key(tags),
        duration = extract_duration(audio),
    )

def scan_aiff(path: str):
    audio = AIFF(path)

def extract_title(tags: dict[str, list[str]] | None):
    if not tags:
        return None
    for key in TITLE_TAGS:
        value = tags.get(key)
        if value:
            try:
                return str(value[0])
            except ValueError:
                    continue
    return None

def extract_artist(tags: dict[str, list[str]] | None):
    if not tags:
        return None
    for key in ARTIST_TAGS:
        value = tags.get(key)
        if value:
            try:
                return str(value[0])
            except ValueError:
                    continue
    return None

def extract_album(tags: dict[str, list[str]] | None):
    if not tags:
        return None
    for key in TITLE_TAGS:
        value = tags.get(key)
        if value:
            try:
                return str(value[0])
            except ValueError:
                    continue
    return None

def extract_release_date(tags: dict[str, list[str]] | None):
    if not tags:
        return None
    for key in RELEASE_TAGS:
        value = tags.get(key)
        if value:
            try:
                return str(value[0])
            except ValueError:
                    continue
    return None  

def extract_duration(audio):
    length = audio.info.length
    return float(int(length // 60) + round(length % 60) / 100)


def extract_bpm(tags: dict[str, list[str]] | None):
    if not tags:
        return None
    for key in BPM_TAGS:
        value = tags.get(key)
        if value:
            try:
                return float(value[0])
            except ValueError:
                continue
    return None

def extract_key(tags: dict[str, list[str]] | None):
    if not tags:
        return None
    for key in KEY_TAGS:
        value = tags.get(key)
        if value:
            try:
                return str(value[0])
            except ValueError:
                    continue
    return None  