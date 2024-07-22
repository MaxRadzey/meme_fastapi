from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from services.database.database import Base, db_helper
from services.memes.router import router as memes_router
from services.users.router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title='Memes API',
    description='Memes API',
    lifespan=lifespan
    )

app.include_router(memes_router)
app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

# uvicorn main:app --reload
