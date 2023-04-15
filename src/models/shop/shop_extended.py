


from typing import Optional
from src.models.shop.shop import ShopBase


class ShopCreate(ShopBase):
    pass


class ShopRead(ShopBase):
    id: int


class ShopUpdate(ShopBase):
    name: Optional[str] = None
    email: Optional[float] = None
    location: Optional[int] = None