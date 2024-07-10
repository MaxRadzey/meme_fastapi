from fastapi import FastAPI
import uvicorn

from services.memes.router import router as memes_router
from services.users.router import router as user_router


app = FastAPI(
    title='Memes API',
    description='Memes API',
    )

app.include_router(memes_router)
app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

# uvicorn main:app --reload
