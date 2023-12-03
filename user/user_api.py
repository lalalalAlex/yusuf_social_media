from fastapi import APIRouter
from datetime import datetime

from database.userservice import edit_user_db, register_db, get_exact_user_db, check_user_email_db, delete_user_db

from user import EditUserValidator, RegisterUserValidator

user_router = APIRouter(prefix='/user', tags=['work with users'])


# Registration of user
@user_router.post('/register')
async def register_user(data: RegisterUserValidator):
    new_user_data = data.model_dump()
    result = register_db(**new_user_data)
    return {'message': result}


@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': "not found"}


@user_router.put('/edit-data')
async def edit_user(data: EditUserValidator):
    change_data = data.model_dump()

    result = edit_user_db(**change_data)

    return {'message': result}


@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)

    if result:
        return {'message': 'User was deleted'}
