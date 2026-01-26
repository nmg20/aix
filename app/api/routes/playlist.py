from app.db.db import get_db
from app.model import Playlist
from app.schema.playlist import PlaylistParse, PlaylistParseResult
from app.crud import playlist_crud
from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix="/playlists", tags=["playlists"])

@router.post("/parse", response_model=PlaylistParseResult,
    status_code=status.HTTP_200_OK)
def parse_playlist(playlist_data: PlaylistParse) -> PlaylistParseResult:
    """
    Toma datos de una playlist para parsear (provider + path) y llama
    al crud que invoca la función de parse del provider correspondiente.
    """
    try:
        print(f"[ENDPOINT]Parsing playlist: {playlist_data.path} on {playlist_data.provider}.\n")
        return playlist_crud.parse(playlist_data)
    except ValueError:
        raise HTTPException(status_code=501, detail="Unsupported operation.")
