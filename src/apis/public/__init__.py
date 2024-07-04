from fastapi import APIRouter
from src.apis.public import category_routes, product_routes, coupon_routes, order_routes, authentication_routes, user_routes, shop_routes

public_router = APIRouter(prefix='/v1')

public_router.include_router(authentication_routes.router)
public_router.include_router(user_routes.router)
public_router.include_router(shop_routes.router)
public_router.include_router(product_routes.router)
public_router.include_router(category_routes.router)
public_router.include_router(order_routes.router)
public_router.include_router(coupon_routes.router)