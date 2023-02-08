from typing import Optional
from sqlmodel import Field, SQLModel


class ProductBase(SQLModel):
    name: str = Field(index=True)
    price: float
    description: Optional[str] = None
    image: Optional[str] = None
    weight: Optional[str] = None


class Product(ProductBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: Optional[int] = Field(default=None, primary_key=True)


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int


class ProductUpdate(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = None
