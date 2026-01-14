from app.model.playlist import Playlist
from app.schemas.playlist import PlaylistCreate, PlaylistInDB
from sqlalchemy.orm import Session
from typing import List, Optional

def create_playlist(db: Session, playlist: PlaylistCreate) -> Playlist:
    playlist_data: dict = playlist.model_dump()
    playlist_orm: Playlist = Playlist(**playlist_data)
    try:
        db.add(playlist_orm)
        db.commit()
        db.refresh(playlist_orm)
    except Exception:
        db.rollback()
        raise
    return playlist_orm

def get_playlist_by_id(db: Session, playlist_id: int) -> Optional[Playlist]:
    return db.query(Playlist).filter(Playlist.id == playlist_id).first()

def get_all_playlists(db: Session) -> List[Playlist]:
    return db.query(Playlist).all()

def get_playlist_by_name(db: Session, name: str) -> Optional[Playlist]:
    return db.query(Playlist).filter(Playlist.name == name).first()
