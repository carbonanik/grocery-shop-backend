from typing import List, Optional

from models.categoty import CategoryRead
from models.product import ProductRead


class CategoryReadWithProduct(CategoryRead):
    products: List[ProductRead] = []


class ProductReadWithCategory(ProductRead):
    category: Optional[CategoryRead] = None
