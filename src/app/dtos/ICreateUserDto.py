from pydantic import BaseModel, EmailStr

# Properties to receive via API on creation
class UserCreateDTO(BaseModel):
    name: str
    email: EmailStr
    password: str