from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.services.youtube import parse_playlist
from app.models import Song

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
