from src.models.product.product import Product
from src.models.category.category import Category
from src.models.coupon.coupon import Coupon
from src.models.order.order import Order
from src.models.shop.shop import Shop
from src.models.user.user import User

from .base_crud import BaseCRUD


product_crud = BaseCRUD(model=Product)
category_crud = BaseCRUD(model=Category)
coupon_crud = BaseCRUD(model=Coupon)
order_crud = BaseCRUD(model=Order)
user_crud = BaseCRUD(model=User)
shop_crud = BaseCRUD(model=Shop)
