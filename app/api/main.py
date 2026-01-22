from fastapi import APIRouter

from app.api.routes import track

api_router = APIRouter()
api_router.include_router(track.router)
# api_router.include_router(playlist.router)