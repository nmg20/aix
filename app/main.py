import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI
from app.routers import playlist
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173"
]

app = FastAPI(
    title="Aix",
    version="0.1.0"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
app.include_router(playlist.router)