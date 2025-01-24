from fastapi import APIRouter, HTTPException, status
from .schemas import RegistrationRequest, RegistrationResponse, GetToken, TokenResponse
from core.database.users import Users

from utils.security import get_hash, get_bearer_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/registration")
async def registrate_user(payload: RegistrationRequest) -> RegistrationResponse:
    new_user = await Users.create(
        username=payload.username,
        hash_password=get_hash(payload.password),
    )

    return RegistrationResponse(
        username=new_user.username
    )


@router.post("/token")
async def get_user_bearer_token(auth_data: GetToken) -> TokenResponse:
    user = await Users.get_or_none(
        username=auth_data.username,
        hash_password=get_hash(auth_data.password)
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect combination of login and password",
        )
    return TokenResponse(**get_bearer_token(user_id=user.id))


