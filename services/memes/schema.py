import re
from datetime import datetime
from typing import Optional

from pydantic import (BaseModel, EmailStr, HttpUrl,
                      SecretStr)


class Memes(BaseModel):
    id: int
    author: int
    creation_date: datetime = datetime.now()
    url: HttpUrl
    description: Optional[str] = None


class MemeCreate(BaseModel):

    url: HttpUrl


class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: SecretStr
