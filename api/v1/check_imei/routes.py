from fastapi import APIRouter, HTTPException
from .schemas import ImeiRequest
from utils.request import get_request

router = APIRouter(prefix="/check-imei", tags=["Check-imei"])


@router.post("")
async def get_information(payload: ImeiRequest):
    response = get_request(token=info.token, device_id=info.imei)
    return response.json()

