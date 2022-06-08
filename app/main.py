from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.core.settings import get_settings
from app.v1.api import router as v1_router


app = FastAPI()
app.include_router(v1_router, prefix='/v1')


register_tortoise(
    app,
    db_url=get_settings().DATABASE_URL,
    modules={'models': get_settings().TORTOISE_MODELS},
    generate_schemas=True,
    add_exception_handlers=True
)
