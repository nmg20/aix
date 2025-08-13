from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select
from app.db import engine
from app.models import Playlist, PlaylistCreate
from typing import List

router = APIRouter(prefix="/playlists", tags=["playlists"])

def get_session():
    with Session(engine) as session:
        yield session

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