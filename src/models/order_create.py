from typing import List
from src.models.coupon import Coupon
from src.models.order import OrderBase
from src.models.orderitem import Orderitem, OrderitemCreate


class OrderCreate(OrderBase):
    order_items: List[Orderitem]
    coupons: List[Coupon]