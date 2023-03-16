import enum
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Enum, Column

from src.models.coupon_order_link import CouponOrderLink


class OrderStatus(enum.Enum):
    PROCESSING = 'PROCESSING'
    IN_TRANSIT = 'IN_TRANSIT'
    DELIVERED = 'DELIVERED'
    CANCELLED = 'CANCELLED'


class OrderBase(SQLModel):
    count: int
    total_price: str
    order_date: str
    order_status: OrderStatus = Field(sa_column=Column(Enum(OrderStatus)))


class Order(OrderBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: Optional[int] = Field(default=None, primary_key=True)
    order_status: OrderStatus = Field(sa_column=Column(Enum(OrderStatus)))
    order_items: List['OrderItem'] = Relationship(back_populates="order_item")
    coupons: List['Coupon'] = Relationship(
        back_populates="coupon",
        link_model=CouponOrderLink,
    )


class CategoryCreate(OrderBase):
    pass


class CategoryRead(OrderBase):
    id: int


class CategoryUpdate(OrderBase):
    count: Optional[int] = None
    total_price: Optional[str] = None
    order_date: Optional[str] = None
    order_status: Optional[OrderStatus] = None
