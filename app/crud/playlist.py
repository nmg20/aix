from app.model.playlist import Playlist
from app.model.playlist_track import PlaylistTrack
from app.crud.base_crud import CrudRepository
from sqlalchemy.orm import Session
from typing import List

class PlaylistCrud(CrudRepository):
    """
    Docstring for PlaylistCrud
    """
    def __init__(self) -> None:
        """
        Inicializa el CRUD como un CRUDRepository del modelo Playlist
        """
        super().__init__(model=Playlist)
    
    def add_track(self, db: Session, 
            playlist_id: int, track_id: int) -> PlaylistTrack | None:
        """
        """
        playlist = super().get_one(db, Playlist.id==playlist_id)
        if playlist is None:
            return None
        position = len(playlist.playlist_tracks) +1
        playlist_track = PlaylistTrack(playlist_id=playlist_id,
            track_id=track_id, position=position)
        playlist.playlist_tracks.append(playlist_track)
        db.commit()
        db.refresh(playlist)
        return playlist_track
    
    def remove_track(self, db: Session, 
            playlist_id: int, track_id: int) -> PlaylistTrack | None:
        """
        """
        playlist = super().get_one(Playlist.id == playlist_id)
        if playlist is None:
            return None
        playlist_track = next(
            (pt for pt in 
             playlist.playlist_tracks if pt.track == track_id),
            None)
        playlist.playlist_tracks.remove(playlist_track)
        db.commit()
        db.refresh(playlist)
    
    def get_tracks(self, db: Session, playlist_id: int) -> List[PlaylistTrack]:
        """
        """
        playlist = super().get_one(Playlist.id == playlist_id)
        if playlist is None:
            return []
        return sorted(playlist.playlist_tracks, key=lambda pt: pt.position)


playlist_crud = PlaylistCrud()