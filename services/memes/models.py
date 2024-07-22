from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from services.database.database import Base


class MemesTable(Base):

    __tablename__ = 'memes'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[int] = mapped_column(nullable=False)
    creation_date: Mapped[datetime] = mapped_column(default=datetime.now())
    url: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(default=None)

    def __str__(self) -> str:
        return self.title
