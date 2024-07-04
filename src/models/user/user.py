from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from src.models.sql_model_common import SQLModelCommon


class UserBase(SQLModelCommon):
    full_name: str
    email: str = Field(index=True)
    phone: str | None = Field(default=None)
    is_active: bool = Field(default=True)


class UserBaseWithPassword(UserBase):
    hashed_password: str


class User(UserBaseWithPassword, table=True):
    __table_args__ = {'extend_existing': True}

    id: int | None = Field(default=None, primary_key=True)
    # orders: List['Order'] = Relationship(back_populates='user')


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int


class UserUpdate(UserBaseWithPassword):
    full_name: str | None = None
    email: str | None = None
    phone: str | None = None
    is_active: bool | None = None