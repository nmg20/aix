from app.db.db import get_db
from app.crud import track as track_crud
from app.schemas.track import TrackInDB
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter()

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
    tracks = track_crud.get_all_tracks(db)
    return tracks