from typing import Optional, List
from typing import Set
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column
from sqlalchemy.dialects import postgresql
from sqlalchemy.types import String
from src.models.sql_model_common import SQLModelCommon



class ProductBase(SQLModelCommon):
    name: str = Field(index=True)
    price: float
    discount_price: float | None = None
    description: str | None = None
    images: Set[str] | None = Field(default=None, sa_column=Column(postgresql.ARRAY(String())))

    # category_id: int | None = Field(default=None, foreign_key="category.id")
    # shop_id: int | None = Field(default=None, foreign_key='shop.id')


class Product(ProductBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: int | None = Field(default=None, primary_key=True)
    # category: Optional['Category'] = Relationship(back_populates="products")
    # order_items: List['Orderitem'] = Relationship(back_populates="product")


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int


class ProductUpdate(ProductBase):
    name: str | None = None
    price: float | None = None


# class ProductReadWithCategory(ProductRead):
#     category: CategoryRead | None = None