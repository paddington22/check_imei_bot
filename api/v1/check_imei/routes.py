from fastapi import APIRouter, HTTPException
from .schemas import ImeiRequest
from utils.request import get_request

router = APIRouter(prefix="/check-imei", tags=["Check-imei"])


@router.post("")
async def get_information(payload: ImeiRequest):
    response = get_request(token=payload.token, device_id=payload.imei)
    return response.json()

