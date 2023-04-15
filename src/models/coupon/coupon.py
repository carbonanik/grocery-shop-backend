import enum
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Enum, Column

from src.models.coupon.coupon_order_link import CouponOrderLink


class CouponStatus(enum.Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'


class CouponEmptyBase(SQLModel):
    pass

class CouponBase(CouponEmptyBase):
    title: Optional[str] = None
    description: Optional[str] = None
    code: Optional[str] = None
    discount: Optional[float] = None
    expire: Optional[str] = None
    status: Optional[CouponStatus] = Field(sa_column=Column(Enum(CouponStatus)))


class Coupon(CouponBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: Optional[int] = Field(default=None, primary_key=True)
    orders: List['Order'] = Relationship(back_populates="coupons", link_model=CouponOrderLink)


