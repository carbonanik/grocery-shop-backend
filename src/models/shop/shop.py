from typing import Optional
from sqlmodel import Field, SQLModel
from src.models.sql_model_common import SQLModelCommon


class ShopBase(SQLModelCommon):
    name: str
    email: str | None = None


class Shop(ShopBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: int | None = Field(default=None, primary_key=True)


class ShopCreate(ShopBase):
    pass


class ShopRead(ShopBase):
    id: int


class ShopUpdate(ShopBase):
    name: str | None = None
    email: float | None = None