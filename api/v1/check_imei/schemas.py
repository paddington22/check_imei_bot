from pydantic import BaseModel, AfterValidator
from typing import Annotated

from utils.imei_validator import is_valid_imei


class ImeiRequest(BaseModel):
    imei: Annotated[str, AfterValidator(is_valid_imei)]
    token: str


class ImeiResponse(BaseModel):
    pass



