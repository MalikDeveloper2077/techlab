from fastapi import APIRouter

from app.core.models.users import User
from app.core.schemas.users import UserPydantic, UserInPydantic


router = APIRouter()


@router.post('/create', response_model=UserPydantic)
async def create_user(user: UserInPydantic):
    new_user = await User.create(**user.dict())
    return await UserPydantic.from_tortoise_orm(new_user)
