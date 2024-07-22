from typing import Annotated
from fastapi import APIRouter, Depends, Path

from services.memes.schema import Meme, CreateMeme
# from services.memes.models import MemesTable


router = APIRouter(
    prefix='/memes',
    tags=['memes']
)

memess: list = [
    {
        'id': 0,
        'author': 1,
        'creation_date': '2024-07-02T19:36:42.984688',
        'url': ('https://sun9-30.userapi.com/impg/m08gGTg4IqlBpGZgW9Re8o3ou_'
                '2IdHAvtKnqOA/jFISLgbJ_Fk.jpg?size=1440x1440&quality=95&sign='
                'd10cc295d38efc1bf62998109ded05de&type=album'),
        'description': 'asdfasdfasdfasd'
        }
]


@router.get('', response_model=list[Meme])
async def get_memes(limit: int = 10, offset: int = 0) -> list[Meme]:
    return memess


@router.get('/{meme_id}', response_model=Meme)
def get_meme(meme_id: Annotated[int, Path(ge=1, lt=1_000_000)]) -> Meme:
    return [meme for meme in memess if meme['id'] == meme_id][0]


@router.post('', response_model=CreateMeme)
def post_memes(meme: Annotated[CreateMeme, Depends()]):
    memess.append(meme)
    return meme


@router.put('/{meme_id}', response_model=Meme)
def put_memes(meme_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return 'put'


@router.delete('/{meme_id}', response_model=Meme)
def delete_memes(meme_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return 'delete'
