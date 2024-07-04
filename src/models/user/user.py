import enum
from sqlmodel import Field
from sqlalchemy import Enum, Column

from src.models.sql_model_common import SQLModelCommon



class UserRole(enum.Enum):
    USER = 'USER'
    VENDOR = 'VENDOR'
    ADMIN = 'ADMIN'


class UserBase(SQLModelCommon):
    full_name: str
    email: str = Field(index=True)
    phone: str | None = Field(default=None)
    is_active: bool = Field(default=True)
    account_type: UserRole | None = Field(default=None, sa_column=Column(Enum(UserRole)))


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