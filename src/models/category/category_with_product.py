from typing import List
from src.models.category.category_extended import CategoryRead
from src.models.product.product_extended import ProductRead


class CategoryReadWithProduct(CategoryRead):
    products: List[ProductRead] = []