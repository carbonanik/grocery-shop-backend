from typing import Optional

from sqlmodel import Field, SQLModel, Relationship

from models.categoty import Category


class ProductBase(SQLModel):
    name: str = Field(index=True)
    price: float
    description: Optional[str] = None
    image: Optional[str] = None
    weight: Optional[str] = None

    category_id: Optional[int] = Field(default=None, foreign_key="category.id")


class Product(ProductBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: Optional[int] = Field(default=None, primary_key=True)

    category: Optional[Category] = Relationship(back_populates="products")


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int


class ProductUpdate(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None



