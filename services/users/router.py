from typing import Annotated
from fastapi import APIRouter, Depends, Path

from services.users.schema import CreateUser, GetUser
from services.users.crud import create_user


router = APIRouter(
    prefix='/users',
    tags=['users']
)

users_list: list = [
    {
        'id': 1,
        'username': 'Max',
        'email': 'max@max.ru',
        'registration_date': '2024-07-02T19:36:42.984688',
        'description': 'asdfasdfasdfasd'
        }
]


@router.get('', response_model=list[GetUser])
async def get_users(limit: int = 10, offset: int = 0) -> list[GetUser]:
    return users_list


@router.get('/{user_id}', response_model=GetUser)
def get_user(user_id: Annotated[int, Path(ge=1, lt=1_000_000)]) -> GetUser:
    return [meme for meme in users_list if meme['id'] == user_id][0]


# @router.post('', response_model=CreateUser)
@router.post('')
def post_user(user: Annotated[CreateUser, Depends()]) -> dict:
    return create_user(user_create=user)
