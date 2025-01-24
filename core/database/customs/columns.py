from typing import Any

from snowflake import SnowflakeGenerator
from tortoise.fields import BigIntField

snowflake_gen = SnowflakeGenerator(42)


def generate_snowflake() -> int:
    return next(snowflake_gen)


class SnowflakeID(BigIntField):
    def __init__(self, **kwargs: Any) -> None:
        kwargs["generated"] = False
        kwargs["default"] = generate_snowflake
        super().__init__(**kwargs)
