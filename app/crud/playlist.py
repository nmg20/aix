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
    CRUD ampliado para la clase Playlist.
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
        Añade un track a una playlist.
        
        Args:
            - db (Session): Sesión de la bd
            - playlist_id (int): Id de la playlist
            - track_id (int): Id del track que añadir a la playlist.
        Return:
            - PlaylistTrack: Clase intermedia de track añadido a la playlist.
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
        Devuelve todos los tracks de una playlist.

        Args:
            - db (Session): Sesión de la bd
            - playlist_id (int): Id de la playlist
        Return:
            - List[PlaylistTrack]: Lista de tracks añadidos a la playlist.
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
        Elimina un track de la playlist.

        Args:
            - db (Session): Sesión de la bd
            - playlist_id (int): Id de la playlist
            - track_id (int): Id del track que quitar a la playlist.
        Return:
            - PlaylistTrack: Track eliminado de la playlist.
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
        Procesa una playlist y lee datos de los tracks que contiene.

        Args:
            - playlist_dat (PlaylistParse): Datos básicos de la playlist (provider + path)
        Return:
            - PlaylistParseResult: Datos obtenidos de los tracks procesados
                -> provider + path + List[ParsedTrack]
        """
        provider = self.providers.get(playlist_data.provider)
        return provider.parse_playlist(playlist_data.path)

    def download(self, db: Session, parsed_playlist: PlaylistParseResult):
        """
        """
        pass

playlist_crud = PlaylistCrud()