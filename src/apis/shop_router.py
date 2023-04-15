from typing import List

from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session, col, select

from src.database.database import get_session
from src.models.shop.shop_extended import ShopCreate, ShopRead, ShopUpdate
from src.crud import shop_crud


router = APIRouter(tags=['Shop API', 'V1'])


@router.post('/shop', status_code=status.HTTP_201_CREATED, response_model=ShopRead)
def create_shop(shop: ShopCreate, session: Session = Depends(get_session)):
    return shop_crud.create(shop, session)


@router.get('/shop', response_model=List[ShopRead])
def read_shops(
    offset: int = 0, 
    limit: int = Query(default=100, lte=100), 
    session: Session = Depends(get_session)
):
    return shop_crud.get(offset, limit, session)


@router.get('/shop/{id}', response_model=ShopRead)
def shop_by_id(id: int, session: Session = Depends(get_session)):
    return shop_crud.get_by_id(id, session)


@router.put('/shop/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=ShopRead)
def shop_update(id: int, shop: ShopUpdate, session: Session = Depends(get_session)):
    return shop_crud.update(id, shop, session)


@router.delete('/shop/{id}', response_model=ShopRead)
def shop_delete(id: int, session: Session = Depends(get_session)):
    return shop_crud.delete(id, session)
