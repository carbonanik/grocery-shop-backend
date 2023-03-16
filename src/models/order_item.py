from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

from src.models.product import Product


class OrderItemBase(SQLModel):
    count: int
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    order_id: Optional[int] = Field(default=None, foreign_key="order.id")


class OrderItem(OrderItemBase, table=True):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'order_item'

    id: Optional[int] = Field(default=None, primary_key=True)
    product: Product = Relationship(back_populates="product")


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemRead(OrderItemBase):
    id: int
    product: Product


class OrderItemUpdate(OrderItemBase):
    count: Optional[int] = None
