from app.model.track import Track
from app.model.track_source import TrackSource
from app.schema.track import TrackCreate, TrackUpdate
from app.crud.base_crud import CrudRepository
from sqlalchemy.orm import Session

class TrackCrud(CrudRepository):
    """
    CRUD ampliado para la clase Track. Tiene en cuenta metadatos y otras
    clases auxiliares de Track.
    """
    def __init__(self) -> None:
        super().__init__(Track)

    def create(self, db: Session, track: TrackCreate,
            ) -> Track:
        """
        Crea el track en la base de datos. Rellena tablas relacionadas
        Args:
            - db (Session): Sesión de la base de datos.
            - track (TrackCreate): Datos del track (+ sources).
        Return:
            - Track: Objeto creado en la base de datos.
        """
        sources_data = track.sources or []

        created_track = Track(
            **track.model_dump(exclude={"sources"})
        )

        for source in sources_data:
            created_track.sources.append(
                TrackSource(**source.model_dump())
            )

        db.add(created_track)
        db.commit()
        db.refresh(created_track)
        return created_track
    
    def update(self, db: Session, track_id: int,
            track_data: TrackUpdate) -> Track | None:
        """
        Actualiza un track en la base de datos. Actualiza tablas relacionadas.

        Args:
            - db (Session): Sesión de la base de datos.
            - track_id (int): Identificador del track a actualizar.
            - track_data (TrackUpdate): Datos a actualizar
        Return:
            - Track: Track en la base de datos con los datos actualizados.
        """
        track = db.get(Track, track_id)
        if track is None:
            return None
        
        for field, data in track_data.model_dump(exclude_unset=True):
            setattr(track, field, data)
        
        db.add(track)
        db.commit()
        db.refresh(track)
        return track
        
track_crud = TrackCrud()