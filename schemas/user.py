from pydantic import BaseModel

# 定義 User 模型
class CreateUser(BaseModel):
    name: str
    email: str
    password: str 


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    
class CreateUserResponse(BaseModel):
    status: str
    message: str
    data: UserResponse
    
class ReadUserResponse(BaseModel):
    status: str
    message: str
    data: list[UserResponse]
    