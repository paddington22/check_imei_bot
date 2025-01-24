import hashlib
from settings.config import settings


def get_hash(secret: str) -> str:
    return hashlib.sha512(secret.encode() + settings.SALT.encode()).hexdigest()
