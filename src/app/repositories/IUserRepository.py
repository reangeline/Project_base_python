from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel
from app.schemas.Users import UserBase
from app.dtos.ICreateUserDto import UserCreateDTO


class IUserRepository(BaseModel, ABC):
    @abstractmethod
    async def create(self, user: UserCreateDTO) -> UserBase:
        pass

    @abstractmethod
    async def findByEmail(self, email: str) -> List[UserBase]:
        pass