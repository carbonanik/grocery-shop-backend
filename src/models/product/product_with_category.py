from typing import Optional
from src.models.category.category_extended import CategoryRead
from src.models.product.product_extended import ProductRead


class ProductReadWithCategory(ProductRead):
    category: Optional[CategoryRead] = None