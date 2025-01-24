from tortoise import fields
from .base import BaseTortoiseModel


class Users(BaseTortoiseModel):
    username = fields.CharField(max_length=255, unique=True)
    hash_password = fields.TextField()
    telegram_id = fields.BigIntField(null=True)
    telegram_context = fields.JSONField(default={})

