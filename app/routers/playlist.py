import os
from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.services.youtube import parse_playlist, download_songs
from app.models import Song
from app.schemas import DownloadRequest

router = APIRouter(prefix="/playlists", tags=["playlists"])

@router.get("/parse")
def analyze_playlist(url: str):
    """
    Analiza una playlist de YouTube y devuelve canciones paginadas.
    """
    try:
        songs = parse_playlist(url)
        return {"songs": songs}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/download")
def download_playlist(request: DownloadRequest):
    urls = request.urls
    download_songs(urls)
    return {"message": f"Descarga completada",
            "urls": urls}