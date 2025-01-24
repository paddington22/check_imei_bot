from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from .schemas import ImeiRequest
from utils.request import get_request
from utils.security import get_user_from_token
from core.database.users import Users

router = APIRouter(prefix="/check-imei", tags=["Check-imei"])


@router.post("")
async def get_information(payload: ImeiRequest, current_user: Annotated[Users, Depends(get_user_from_token)]):
    response = get_request(token=payload.token, device_id=payload.imei)
    return response.json()

