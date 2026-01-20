from .db.session import engine
from .db.base_class import Base
from .model.playlist import Playlist
from .model.track import Track
from .model.track_source import TrackSource
from .model.track_metadata import TrackMetadata
from .model.audio_feature import AudioFeature
from .model.user import User

Base.metadata.create_all(bind=engine)