from pydantic import BaseModel, Field
import datetime

class TrackSourceBase(BaseModel):
    provider: str
    path: str
    format: str | None
    bitrate: str | None
    sample_rate: int | None

class TrackSourceCreate(TrackSourceBase):
    pass

class TrackSourceUpdate(BaseModel):
    pass

class TrackSourceInDB(TrackSourceBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True