from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl


class Meme(BaseModel):

    id: int
    author: int
    creation_date: datetime = datetime.now()
    url: HttpUrl
    description: Optional[str] = None


class CreateMeme(BaseModel):

    url: HttpUrl
