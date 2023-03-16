from typing import List, Optional

from src.models.category import CategoryRead
from src.models.product import ProductRead


class CategoryReadWithProduct(CategoryRead):
    products: List[ProductRead] = []


class ProductReadWithCategory(ProductRead):
    category: Optional[CategoryRead] = None
