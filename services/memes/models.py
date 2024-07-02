from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

engine = create_async_engine(
    'sqlite+aiosqlite:///memes.db'
)

session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class MemesTable(Base):

    __tablename__ = 'memes'
    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[int] = mapped_column(nullable=False)
    creation_date: Mapped[datetime] = mapped_column(default=datetime.now())
    url: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(default=None)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
