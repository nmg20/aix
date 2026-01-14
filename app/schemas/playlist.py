from pydantic import BaseModel, Field
import datetime

class PlaylistBase(BaseModel):
    name: str

class PlaylistCreate(PlaylistBase):
    author: str
    path: str

class PlaylistInDB(PlaylistBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True