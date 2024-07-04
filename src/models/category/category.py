from sqlmodel import Field
from src.models.sql_model_common import SQLModelCommon


class CategoryBase(SQLModelCommon):
    name: str = Field(index=True)
    description: str | None = None
    image: str | None = None

class Category(CategoryBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: int | None = Field(default=None, primary_key=True)
    parent_id: int | None = Field(default=None, foreign_key="category.id")

    # products: List['Product'] = Relationship(back_populates="category")


class CategoryCreate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int


class CategoryUpdate(CategoryBase):
    name: str | None = None

# class CategoryReadWithProduct(CategoryRead):
#     products: List[ProductRead] = []