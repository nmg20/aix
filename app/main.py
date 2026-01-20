from fastapi import FastAPI
from app.api.routes.track import router as track_router

app = FastAPI()

app.include_router(track_router, prefix="/tracks", tags=["track"])

@app.get('/')
def root():
    return {"message": "Hello World!"}