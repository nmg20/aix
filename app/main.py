import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI
from app.routers import playlist

app = FastAPI(
    title="Aix",
    version="0.1.0"
    )

app.include_router(playlist.router)