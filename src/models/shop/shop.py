


from typing import Optional
from sqlmodel import Field, SQLModel


class ShopBase(SQLModel):
    name: str
    email: str
    location: Optional[str]


class Shop(ShopBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: Optional[int] = Field(default=None, primary_key=True)