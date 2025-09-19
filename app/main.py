import sys
import os
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routers import playlist
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination # type: ignore

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

if getattr(sys, 'frozen', False):
    base_path = os.path.join(sys._MEIPASS, "frontend", "dist") # type: ignore
else:
    base_path = "frontend/dist"

app.mount("/assets", StaticFiles(directory=os.path.join(base_path, "assets")), name="assets")
app.mount("/", StaticFiles(directory=base_path, html=True), name="root")

@app.get("/")
def serve_frontend():
    return FileResponse("frontend/dist/index.html")

add_pagination(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)