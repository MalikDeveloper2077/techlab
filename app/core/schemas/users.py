from pydantic import EmailStr
from tortoise.contrib.pydantic import pydantic_model_creator

from app.core.models.users import User


UserBase_Pydantic = pydantic_model_creator(User, name='UserIn', exclude=('id', 'email',))


class UserInPydantic(UserBase_Pydantic):
    email: EmailStr


class UserPydantic(UserInPydantic):
    id: int
