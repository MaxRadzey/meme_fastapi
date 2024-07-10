from annotated_types import MaxLen, MinLen
from datetime import datetime
from typing import Optional, Annotated

from pydantic import BaseModel, EmailStr, SecretStr


class GetUser(BaseModel):

    id: int
    username: Annotated[str, MaxLen(25), MinLen(3)]
    email: EmailStr
    registration_date: datetime = datetime.now()
    description: Optional[str] = None


class CreateUser(BaseModel):

    username: Annotated[str, MaxLen(25), MinLen(3)]
    # password: SecretStr
    email: EmailStr
    registration_date: datetime = datetime.now()
    description: Optional[str] = None
