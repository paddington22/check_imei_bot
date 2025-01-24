import hashlib
import jwt
from jwt import PyJWTError
from datetime import datetime, timezone, timedelta
from settings.config import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from core.database.users import Users

bearer_scheme = HTTPBearer()
TIMEZONE = timezone.utc


def get_hash(secret: str) -> str:
    return hashlib.sha512(secret.encode() + settings.SALT.encode()).hexdigest()


def get_bearer_token(user_id: int) -> dict:
    expire = datetime.now(tz=TIMEZONE) + timedelta(seconds=settings.ACCESS_TOKEN_EXPIRE_SECONDS)
    payload = {
        "user_id": str(user_id),
        "exp": int(expire.timestamp()),
    }
    access_token = jwt.encode(
        payload={"payload": payload},
        key=settings.ACCESS_TOKEN_SECRET.get_secret_value(),
        algorithm="HS256",
    )
    return {"access_token": access_token, "token_type": "Bearer"}


async def get_user_from_token(token: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token.credentials, settings.ACCESS_TOKEN_SECRET.get_secret_value(), algorithms=["HS256"])
    except PyJWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e)) from e

    payload = payload.get("payload", {})
    user_id: str = payload.get("user_id")
    if not user_id:
        raise credentials_exception

    user_obj = await Users.get_or_none(
        id=user_id,
    )
    if not user_obj:
        raise credentials_exception
    return user_obj
