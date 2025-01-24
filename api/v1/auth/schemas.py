from pydantic import BaseModel


class RegistrationRequest(BaseModel):
    telegram_username: str
    password: str


class RegistrationResponse(BaseModel):
    telegram_username: str


class GetToken(RegistrationRequest):
    pass


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


