from tortoise.models import Model

from core.database.customs.columns import SnowflakeID, generate_snowflake


class BaseTortoiseModel(Model):
    id = SnowflakeID(pk=True)

    class Meta:
        abstract = True

    @staticmethod
    def generate_id():
        return generate_snowflake()
