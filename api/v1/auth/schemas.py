from pydantic import BaseModel


class RegistrationRequest(BaseModel):
    username: str
    password: str


class RegistrationResponse(BaseModel):
    username: str
