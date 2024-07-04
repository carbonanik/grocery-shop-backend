import enum
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Enum, Column
from src.models.sql_model_common import SQLModelCommon


# from src.models.coupon.coupon_order_link import CouponOrderLink


# class CouponStatus(enum.Enum):
#     ACTIVE = 'ACTIVE'
#     INACTIVE = 'INACTIVE'


class CouponEmptyBase(SQLModelCommon):
    pass

class CouponBase(CouponEmptyBase):
    code: str | None = None
    description: str | None = None
    discount: float | None = None
    expire: str | None = None
    # status: Optional[CouponStatus] = Field(sa_column=Column(Enum(CouponStatus)))


class Coupon(CouponBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: int | None = Field(default=None, primary_key=True)
    # orders: List['Order'] = Relationship(back_populates="coupons", link_model=CouponOrderLink)


class CouponCreate(CouponBase):
    pass

# class CouponCreateWithOrder(CouponEmptyBase):
#     id: int

class CouponRead(CouponBase):
    id: int


class CouponUpdate(CouponBase):
    pass

# class CouponOrderLink(SQLModel, table=True):
#     coupon_id: Optional[int] = Field(
#         default=None, foreign_key="coupon.id", primary_key=True
#     )
#     order_id: Optional[int] = Field(
#         default=None, foreign_key="order.id", primary_key=True
#     )
