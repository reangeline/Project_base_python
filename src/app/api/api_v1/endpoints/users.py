from typing import Any

from fastapi import APIRouter

from app.dtos.ICreateUserDto import UserCreateDTO 
from app.controllers.UserController import UserController
from app import schemas

router = APIRouter()
userController = UserController()

@router.post("/", response_model=schemas.UserBase)
async def create_user(
    user: UserCreateDTO,
) -> Any:
    """
    Create new user.
    """
    createdUser = await userController.create(user)


    return createdUser
