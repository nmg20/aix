from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel

from enum import Enum

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str

    playlists: list["Playlist"] = Relationship(back_populates="author")

class Playlist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    created: datetime = Field(default_factory=datetime.now)
    
    author_id: int = Field(foreign_key="user.id")
    author: Optional[User] = Relationship(back_populates="playlists")

class Artist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class Album(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    artist_id: int = Field(foreign_key="artist.id")
    released: datetime

class Song(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    artist_id: int = Field(foreign_key="artist.id")
    album_id: int = Field(foreign_key="album.id")
    duration: float

class SongInfo(BaseModel):
    path: str
    title: Optional[str] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    release: Optional[str] = None
    bpm: Optional[float] = None
    key: Optional[str] = None
    duration: Optional[float] = None
    tags: Optional[List[str]] = None

################################################################

class UserCreate(SQLModel):
    name: str
    password: str

class PlaylistCreate(SQLModel):
    name: str
    author_id: int

class ArtistCreate(SQLModel):
    name: str

class AlbumCreate(SQLModel): 
    title: str
    artist_id: int
    released: datetime

class SongCreate(SQLModel):
    title: str
    artist_id: int
    album_id: int
    duration: float

################################################################

class UserRead(SQLModel):
    name: str
    password: str

class PlaylistRead(SQLModel):
    name: str
    author_id: int

class ArtistRead(SQLModel):
    name: str

class AlbumRead(SQLModel): 
    title: str
    artist_id: int
    released: datetime

class SongRead(SQLModel):
    title: str
    artist_id: int
    album_id: int
    duration: float