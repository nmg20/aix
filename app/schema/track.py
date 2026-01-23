from pydantic import BaseModel, Field
from app.schema.track_source import TrackSourceCreate, TrackSourceRead
import datetime
from typing import List

class TrackBase(BaseModel):
    title: str
    duration: float

class TrackCreate(TrackBase):
    sources: list[TrackSourceCreate] | None = None

class TrackUpdate(BaseModel):
    title: str | None = None
    duration: float | None = None

class TrackRead(TrackBase):
    id: int
    sources: List[TrackSourceRead] | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True