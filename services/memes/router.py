from typing import Annotated
from fastapi import APIRouter, Depends

from services.memes.schema import Memes


router = APIRouter(
    prefix='/memes'
)

memess: list = []


@router.get('')
async def get_memes(meme: Memes):
    memess
    return 'Get'


@router.get('')
def get_meme(id: int):
    return 'Get'


@router.post('')
def post_memes(meme: Annotated[Memes, Depends()]):
    memess.append(meme)
    return 'post'


@router.put('')
def put_memes(id: int):
    return 'put'


@router.delete('')
def delete_memes(id: int):
    return 'delete'
