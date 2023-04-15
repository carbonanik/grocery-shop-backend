from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship


class CategoryBase(SQLModel):
    name: str = Field(index=True)
    description: Optional[str] = None
    image: Optional[str] = None

class Category(CategoryBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: Optional[int] = Field(default=None, primary_key=True)

    products: List['Product'] = Relationship(back_populates="category")

