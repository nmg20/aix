from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select
from typing import List, Optional

from app.db import engine, get_session
from app.models import Playlist, PlaylistCreate

from services.local import sync_playlist

router = APIRouter(prefix="/playlists", tags=["playlists"])

@router.get("/", status_code=status.HTTP_201_CREATED, response_model=List[Playlist])
def list_playlists(session: Session = Depends(get_session)):
    playlists = session.exec(select(Playlist)).all()
    return playlists

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_playlist(playlist: PlaylistCreate, session: Session = Depends(get_session)):
    db_playlist = Playlist(
        name = playlist.name,
        author_id = playlist.author_id,
    )
    session.add(db_playlist)
    session.commit()
    session.refresh(db_playlist)
    return db_playlist

@router.post("/sync", status_code=status.HTTP_202_ACCEPTED)
def sync(path: Optional[str] = None):
    result = sync_playlist(path)
    return 