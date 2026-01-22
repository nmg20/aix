from app.model.playlist import Playlist
from app.crud.base_crud import CrudRepository

playlist_crud = CrudRepository(model=Playlist)