from app.dtos.ICreateUserDto import UserCreateDTO
from app.services.CreateUserService import CreateUserService
from app.repositories.UserRepository import UserRepository 
from app.schemas.Users import UserBase


class UserController:
    async def create(self, user: UserCreateDTO) -> UserBase:
        userRepository = UserRepository()

        createUser = CreateUserService(userRepository)

        createdUser = await createUser.execute(user)

        userResponse = {
            'id': str(createdUser.id),
            'name': user.name, 
            'email': user.email, 
            'password': user.password
            }

        return userResponse