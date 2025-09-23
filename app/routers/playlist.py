import os
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.services.providers.youtube import parse_playlist, download_songs
from app.models import Song
from app.schemas import DownloadRequest, Song
from fastapi_pagination import Page, paginate # type: ignore
from app.services.playlist_service import PlaylistService

router = APIRouter(prefix="/playlists", tags=["playlists"])
service = PlaylistService()

@router.get("/parse", response_model=Page[Song])
def analyze_playlist(
    url: str,
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    search: Optional[str] = None,
    # added_before: Optional[str] = None,
    # added_after: Optional[str] = None
    ):
    """
    Devuelve la lista de canciones contenida en la playlist identificada
    por la URL. Las devuelve:
        - paginadas
        - filtradas por nombre/artista
        - filtradas por un rango de fechas
    """
    try:
        songs = service.parse_playlist(url, search)
        page_songs, total = service.get_page(songs, page, size)
        return paginate(page_songs)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/download")
def download_playlist(request: DownloadRequest):
    try:
        songs = []
        for url in request.urls:
            songs.extend(
                service.parse_playlist(url)
            )
        service.download_songs(songs)
        return {
            "message": "Descarga completada",
            "urls": request.urls
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))