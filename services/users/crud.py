from services.users.schema import CreateUser


def create_user(user_create: CreateUser) -> dict:
    user = user_create.model_dump()
    return {
        'Sucsses': True,
        'user': user
    }
