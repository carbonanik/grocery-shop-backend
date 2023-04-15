from typing import Optional, List
from pydantic import BaseModel

from sqlmodel import Field, SQLModel, Relationship


class ProductBase(SQLModel):
    name: str = Field(index=True)
    price: float
    description: Optional[str] = None
    image: Optional[str] = None
    weight: Optional[str] = None

    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    shop_id: Optional[int] = Field(default=None, foreign_key='shop.id')


class Product(ProductBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: Optional[int] = Field(default=None, primary_key=True)
    category: Optional['Category'] = Relationship(back_populates="products")
    order_items: List['Orderitem'] = Relationship(back_populates="product")


