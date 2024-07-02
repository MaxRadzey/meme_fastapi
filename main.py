from fastapi import FastAPI
# from fastapi.concurrency import asynccontextmanager
# from pydantic import BaseModel, EmailStr, HttpUrl, constr, field_validator

from services.memes.router import router as memes_router
# from services.memes.database import create_tables


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await create_tables()
#     yield

app = FastAPI(
    title='Memes API',
    description='Memes API',
    )

app.include_router(memes_router)


# uvicorn main:app --reload
