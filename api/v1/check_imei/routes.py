from fastapi import APIRouter, HTTPException


router = APIRouter(prefix="/check-imei", tags=["Check-imei"])


@router.post("")
async def get_information():
    pass
