from typing import List

from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session

from src.database.database import get_session
from src.models.product.product import *
from src.crud import product_crud

router = APIRouter(prefix='/public', tags=['Product API'])


@router.post('/product', status_code=status.HTTP_201_CREATED, response_model=ProductRead)
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    return product_crud.create(product, session)


@router.get('/product', response_model=List[ProductRead])
# @router.get('/product/with-category', response_model=List[ProductReadWithCategory])
def read_products(
    offset: int = 0, 
    limit: int = Query(default=100, lte=100), 
    session: Session = Depends(get_session)
):
    return product_crud.get(offset, limit, session)


@router.get('/product/{id}', response_model=ProductRead)
# @router.get('/product/{id}/with-category', response_model=ProductReadWithCategory)
def product_by_id(id: int, session: Session = Depends(get_session)):
    return product_crud.get_by_id(id, session)


@router.put('/product/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=ProductRead)
def product_update(id: int, product: ProductUpdate, session: Session = Depends(get_session)):
    return product_crud.update(id, product, session)


@router.delete('/product/{id}', response_model=ProductRead)
def product_delete(id: int, session: Session = Depends(get_session)):
    return product_crud.delete(id, session)
