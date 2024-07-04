from typing import Optional, List
from pydantic import BaseModel

from sqlmodel import Field, SQLModel, Relationship
from src.models.order.order import Order
from src.models.product.product import Product


class OrderitemBase(SQLModel):
    count: int
    # product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    # order_id: Optional[int] = Field(default=None, foreign_key="order.id")


class Orderitem(OrderitemBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: Optional[int] = Field(default=None, primary_key=True)
    # order: Optional[Order] = Relationship(back_populates="order_items")
    # product: Optional[Product] = Relationship(back_populates="order_items")


class OrderitemCreate(OrderitemBase):
    pass


class OrderitemRead(OrderitemBase):
    id: int
    # product: Optional[Product]
