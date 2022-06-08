from tortoise.models import Model
from tortoise import fields

from app.core.settings import get_settings


class User(Model):
    id = fields.IntField(pk=True)
    uuid = fields.UUIDField()
    email = fields.CharField(50)

    class Meta:
        table = get_settings().USERS_TABLE_NAME

    def __str__(self):
        return self.email
