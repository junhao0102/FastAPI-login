from pydantic import BaseModel

class Login(BaseModel):
    name: str
    password: str


class LoginResponse(BaseModel):
    status: str
    message: str
