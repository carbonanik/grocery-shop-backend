from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


class UserBase(SQLModel):
    full_name: str
    email: str = Field(index=True)
    is_active: bool = Field(default=True)

class UserBaseWithPassword(UserBase):
    hashed_password: str


class User(UserBaseWithPassword, table=True):
    __table_args__ = {'extend_existing': True}

    id: Optional[int] = Field(default=None, primary_key=True)
    orders: List['Order'] = Relationship(back_populates='user')