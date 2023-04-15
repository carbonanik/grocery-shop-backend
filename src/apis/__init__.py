from fastapi import APIRouter
from src.apis import category_routes, product_routes, coupon_routes, order_routes, authentication_routes, user_routes

router = APIRouter(prefix='/v1')

router.include_router(authentication_routes.router)
router.include_router(user_routes.router)
router.include_router(product_routes.router)
router.include_router(category_routes.router)
router.include_router(order_routes.router)
router.include_router(coupon_routes.router)