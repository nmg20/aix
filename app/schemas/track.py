from pydantic import BaseModel, Field
import datetime

class TrackBase(BaseModel):
    title: str
    duration: int

class TrackCreate(TrackBase):
    pass

class TrackInDB(TrackBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True