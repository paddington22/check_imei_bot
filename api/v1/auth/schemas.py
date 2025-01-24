from pydantic import BaseModel


class RegistrationRequest(BaseModel):
    username: str
    password: str


class RegistrationResponse(BaseModel):
    username: str


class GetToken(RegistrationRequest):
    pass


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


