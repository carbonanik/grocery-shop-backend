import enum
from typing import Optional, List
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Enum, Column

from src.models.category import Category
from src.models.coupon_order_link import CouponOrderLink


class CouponStatus(enum.Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'


class CouponBase(SQLModel):
    title: str = Field(index=True)
    description: Optional[str] = None
    code: str
    discount: float
    expire: Optional[str] = None
    status: CouponStatus = Field(sa_column=Column(Enum(CouponStatus)))


class Coupon(CouponBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: Optional[int] = Field(default=None, primary_key=True)
    orders: List['Order'] = Relationship(back_populates="coupons", link_model=CouponOrderLink)


class CouponCreate(CouponBase):
    pass


class CouponRead(CouponBase):
    id: int


class CouponUpdate(CouponBase):
    pass
