from typing import List
from mongoengine.connection import connect
from app.repositories.IUserRepository import IUserRepository
from app.dtos.ICreateUserDto import UserCreateDTO
from app.schemas.Users import UserBase, User


class UserRepository(IUserRepository):
    def __init__(self):
        connect('mufasa', host='127.0.0.1', port=27017)

    async def create(self, user: UserCreateDTO) -> UserBase:
        createUser = User(name=user.name, 
                    email=user.email, 
                    password=user.password)

        createUser.save()
        createUser.id

        return createUser
     
    async def findByEmail(self, email: str) -> List[UserBase]:
        return User.objects(email=email)
    






