from typing import Optional
from src.models.product.product import ProductBase


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int


class ProductUpdate(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None