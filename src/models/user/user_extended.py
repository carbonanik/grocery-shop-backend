

from typing import Optional
from src.models.user.user import UserBase, UserBaseWithPassword


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int


class UserUpdate(UserBaseWithPassword):
    name: Optional[str]
    email: Optional[str]
