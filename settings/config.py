from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", env_file_encoding="utf-8"
    )

    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_MAX_POOLSIZE: int = 10

    CLIENTS_BOT_TOKEN: str
    BOT_WEBHOOK_URL: str

    def pg_conn(self):
        return {
            "host": self.POSTGRES_HOST,
            "port": self.POSTGRES_PORT,
            "user": self.POSTGRES_USER,
            "password": self.POSTGRES_PASSWORD,
            "database": self.POSTGRES_DB,
            "maxsize": self.POSTGRES_MAX_POOLSIZE,
        }


settings = Settings()

REGISTERED_MODELS_LIST = [
    "core.database.users",
]

TORTOISE_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "statement_cache_size": 0,
                **settings.pg_conn(),
            },
        },
    },
    "apps": {
        "models": {
            "models": [*REGISTERED_MODELS_LIST, "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "UTC",
}
