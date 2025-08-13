import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_PLAYLIST_PATH = os.getenv("DEFAULT_PLAYLIST_PATH", "C:/Users/nicog/Desktop/test/")
SUPPORTED_FORMATS = [".mp3", ".wav", ".flac", ".opus", ".aiff"]