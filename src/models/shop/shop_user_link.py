import enum
from typing import Optional
from sqlalchemy import Column, Enum
from sqlmodel import Field, SQLModel


class ShopRole(enum.Enum):
    OWNER = 'OWNER'
    ADMIN = 'ADMIN'

class ShopUserLink(SQLModel, table=True):
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    shop_id: Optional[int] = Field(
        default=None, foreign_key="shop.id", primary_key=True
    )
    shop_role: Optional[ShopRole] = Field(sa_column=Column(Enum(ShopRole)))