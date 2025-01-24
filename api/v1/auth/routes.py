from fastapi import APIRouter, HTTPException
from .schemas import RegistrationRequest, RegistrationResponse
from core.database.users import Users

from utils.security import get_hash

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