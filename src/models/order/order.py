import enum
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Enum, Column
from src.models.sql_model_common import SQLModelCommon

# from src.models.coupon.coupon_order_link import CouponOrderLink


class OrderStatus(enum.Enum):
    PROCESSING = 'PROCESSING'
    IN_TRANSIT = 'IN_TRANSIT'
    DELIVERED = 'DELIVERED'
    CANCELLED = 'CANCELLED'


class OrderBase(SQLModelCommon):
    total_item: int | None = None
    total_payable_price: float | None = None
    order_date: str | None = None
    order_status: OrderStatus | None = Field(default=None, sa_column=Column(Enum(OrderStatus)))

    # user_id: Optional[int] = Field(default=None, foreign_key='user.id')


class Order(OrderBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: int | None = Field(default=None, primary_key=True)
    # order_items: List['Orderitem'] = Relationship(back_populates="order")
    # coupons: List['Coupon'] = Relationship(
    #     back_populates='orders', link_model=CouponOrderLink)
    # user: Optional['User'] = Relationship(back_populates='orders')


class OrderRead(OrderBase):
    id: int
    # order_items: List[OrderitemRead]
    # coupons: List[Coupon]


class OrderCreate(OrderBase):
    # order_items: List[OrderitemCreateWithOrder]
    # coupons: List[CouponCreateWithOrder]
    pass


class OrderUpdate(OrderBase):
    pass