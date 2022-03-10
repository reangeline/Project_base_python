from fastapi import HTTPException

from app.repositories.IUserRepository import IUserRepository 
from app.dtos.ICreateUserDto import UserCreateDTO
from app.schemas.Users import UserBase


class CreateUserService():
    def __init__(self, userRepository: IUserRepository) -> UserBase:
        self.userRepository = userRepository

    async def execute(self, user: UserCreateDTO):
        isUserExist = await self.userRepository.findByEmail(user.email)

        if isUserExist:
            raise HTTPException(
                status_code=400,
                detail="The user with this email already exists in the system.",
            )


        createdUser = await self.userRepository.create(user)
        
        return createdUser
