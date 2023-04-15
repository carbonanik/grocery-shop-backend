import enum
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Enum, Column

from src.models.coupon.coupon_order_link import CouponOrderLink


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

    user_id: Optional[int] = Field(default=None, foreign_key='user.id')


class Order(OrderBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: Optional[int] = Field(default=None, primary_key=True)
    order_items: List['Orderitem'] = Relationship(back_populates="order")
    coupons: List['Coupon'] = Relationship(
        back_populates='orders', link_model=CouponOrderLink)
    user: Optional['User'] = Relationship(back_populates='orders')
