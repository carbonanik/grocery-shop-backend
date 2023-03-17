from typing import List
from src.models.coupon import Coupon
from src.models.orderitem import Orderitem, OrderitemRead
from src.models.order import OrderBase


class OrderRead(OrderBase):
    id: int
    order_items: List[OrderitemRead]
    coupons: List[Coupon]