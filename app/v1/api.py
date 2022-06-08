from fastapi import APIRouter

from app.v1.endpoints.users import router as users_router


router = APIRouter()
router.include_router(users_router, prefix='/users', tags=['Users'])
