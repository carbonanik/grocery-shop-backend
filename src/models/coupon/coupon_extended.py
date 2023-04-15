from src.models.coupon.coupon import CouponBase, CouponEmptyBase


class CouponCreate(CouponBase):
    pass

class CouponCreateWithOrder(CouponEmptyBase):
    id: int

class CouponRead(CouponBase):
    id: int


class CouponUpdate(CouponBase):
    pass
