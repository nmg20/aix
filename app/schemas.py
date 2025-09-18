from pydantic import BaseModel
from typing import List

class DownloadRequest(BaseModel):
    urls: List[str]