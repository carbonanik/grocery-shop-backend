from typing import List
from src.models.coupon.coupon import Coupon
from src.models.coupon.coupon_extended import CouponCreateWithOrder
from src.models.order.order import OrderBase
from src.models.order.orderitem import OrderitemCreateWithOrder


class OrderCreate(OrderBase):
    order_items: List[OrderitemCreateWithOrder]
    coupons: List[CouponCreateWithOrder]