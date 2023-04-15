from typing import List, Optional
from src.models.category.category import Category, CategoryBase


class CategoryCreate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int


class CategoryUpdate(CategoryBase):
    name: Optional[str] = None
