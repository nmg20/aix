from app.db.db import get_db
from app.model import Track
from app.crud.track import track_crud as crud
from app.schemas.track import TrackInDB, TrackCreate, TrackUpdate
from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.orm import Session

router = APIRouter(prefix="/tracks", tags=["tracks"])

@router.get("/", response_model=list[TrackInDB],
    status_code=status.HTTP_200_OK)
def fetch_all_tracks(db: Session = Depends(get_db)):
    """
    Estraer todos los tracks.

    TODO: añadir limit, offset y skip
    
    Parameters:
        db (Session): La sesión de la bd
    
    Returns:
        list[TrackInDB]: Lista con la representación de los tracks en la bd.
    """
    tracks = crud.get_many(db)
    return tracks

@router.get("/{track_id}", response_model=TrackInDB,
    status_code=status.HTTP_200_OK)
def fetch_track_by_id(track_id: int, db: Session = Depends(get_db)):
    """
    Obtener el track dado un identificador si existe.
    
    Parameters:
        track_id (int): Identificador del track
        db (Session): La sesión de la bd
    
    Returns:
        TrackInDB: Track con el id en la bd.
    """
    track = crud.get_one(db, id=track_id)
    if track is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Track con id {track_id} no encontrado."
        )
    return track

@router.get("/title/{title}", response_model=TrackInDB,
    status_code=status.HTTP_200_OK)
def fetch_track_by_title(track_title: str, 
    db: Session = Depends(get_db)):
    """
    Obtener el track con track_title como título.
    
    Parameters:
        title (str): Identificador del track
        db (Session): La sesión de la bd
    
    Returns:
        TrackInDB: Track con el id en la bd.
    """
    track = crud.get_one(db, title=track_title)
    if track is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Track con título {track_title} no encontrado."
        )
    return track

@router.post("/", response_model=TrackInDB, 
    status_code=status.HTTP_201_CREATED)
def create_track(track: TrackCreate, 
        db: Session = Depends(get_db)):
    """
    Crea un track desde cero.
    
    Parameters:
        track (Track): Track básico
        db (Session): La sesión de la bd
    
    Returns:
        TrackInDB: Track en la bd.
    """
    created_track = crud.create(db, track)
    return created_track

@router.put("/{track_id}", response_model=TrackInDB, 
    status_code=status.HTTP_200_OK)
def update_track(track_id: int,
        track_update: TrackUpdate,
        db: Session = Depends(get_db)):
    """
    Actualiza un track en base de datos.
    
    Parameters:
        track_id (int): Identificador del track
        track_update (TrackUpdate): Data/Schema del track actualizado
        db (Session): La sesión de la bd
    
    Returns:
        TrackInDB: Track en la bd.
    """
    track = crud.get_one(db, Track.id == track_id)
    if track is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El track con id {track_id} no existe."
        )
    updated_track= crud.update(db, track_id, track_update)
    return updated_track

@router.delete("/{track_id}", response_model=dict, 
    status_code=status.HTTP_200_OK)
def delete_track(track_id: int,
        db: Session = Depends(get_db)):
    """
    Borra un track de la base de datos.
    
    Parameters:
        track_id (int): Identificador del track
        db (Session): La sesión de la bd
    
    Returns:
        TrackInDB: Información del track borrado.
    """
    track = crud.get_one(db, Track.id == track_id)
    if track is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El track con id {track_id} no existe."
        )
    try:
        deleted_track = crud.delete(db, track_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"No se pudo borrar el track con id {track_id}. Error: {str(e)}"
        ) from e
    return {"detail": f"Track con id {track_id} borrado."}