from pydantic import BaseModel, Field
import datetime

class TrackBase(BaseModel):
    title: str
    duration: float

class TrackCreate(TrackBase):
    pass

class TrackUpdate(BaseModel):
    title: str | None = None
    duration: float | None = None

class TrackInDB(TrackBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True