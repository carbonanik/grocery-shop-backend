from typing import List
from src.models.coupon.coupon import Coupon
from src.models.order.orderitem import Orderitem, OrderitemRead
from src.models.order.order import OrderBase


class OrderRead(OrderBase):
    id: int
    order_items: List[OrderitemRead]
    coupons: List[Coupon]