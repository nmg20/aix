from app.model.playlist import Playlist
from app.model.playlist_track import PlaylistTrack
from app.schema.playlist import PlaylistParse, PlaylistParseResult
from app.schema.track import TrackUpdate, TrackRead
from app.crud.base_crud import CrudRepository
from sqlalchemy.orm import Session
from typing import List
from app.providers import providers_registry

class PlaylistCrud(CrudRepository):
    """
    Docstring for PlaylistCrud
    """
    def __init__(self) -> None:
        """
        Inicializa el CRUD como un CRUDRepository del modelo Playlist
        """
        super().__init__(model=Playlist)
        self.providers = providers_registry
    
    # Expanded basic playlist CRUD

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
    
    def get_tracks(self, db: Session, playlist_id: int) -> List[PlaylistTrack]:
        """
        """
        playlist = super().get_one(Playlist.id == playlist_id)
        if playlist is None:
            return []
        return sorted(playlist.playlist_tracks, key=lambda pt: pt.position)

    def update_track(self, db: Session, playlist_id: int, track_data: TrackUpdate) -> TrackRead | None:
        """
        """
        pass

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
    
    # Playlist processing functions 

    def parse(self, playlist_data: PlaylistParse) -> PlaylistParseResult:
        """
        """
        print(f"[CRUD]Parsing playlist: {playlist_data.path} on {playlist_data.provider}.\n")
        provider = self.providers.get(playlist_data.provider)
        return provider.parse_playlist(playlist_data.path)

    def download(self, db: Session, parsed_playlist: PlaylistParseResult):
        """
        """
        pass

playlist_crud = PlaylistCrud()