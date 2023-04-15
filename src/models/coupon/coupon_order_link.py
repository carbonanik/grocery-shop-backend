from typing import Optional

from sqlmodel import Field, SQLModel


class CouponOrderLink(SQLModel, table=True):
    coupon_id: Optional[int] = Field(
        default=None, foreign_key="coupon.id", primary_key=True
    )
    order_id: Optional[int] = Field(
        default=None, foreign_key="order.id", primary_key=True
    )
