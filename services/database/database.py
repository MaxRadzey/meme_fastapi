from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from .settings import settings
# from dotenv import load_dotenv

# import os

# load_dotenv()

# DB_NAME = os.environ.get('DB_NAME')
# DB_USER = os.environ.get('DB_USER')
# DB_PASSWORD = os.environ.get('DB_PASSWORD')
# DB_HOST = os.environ.get('DB_HOST')
# DB_PORT = os.environ.get('DB_PORT')

# engine = create_async_engine(
#     'sqlite+aiosqlite:///memes.db'
# )

# session = async_sessionmaker(
#     engine, expire_on_commit=False
# )


class Base(DeclarativeBase):
    pass


class DataBaseHelper:
    def __init__(self, url: str, echo: bool = False) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


db_helper = DataBaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
    )
