from typing import List
from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session

from src.database.database import get_session
from src.models.category.category import CategoryCreate, CategoryRead, CategoryUpdate
from src.crud import category_crud


router = APIRouter(prefix='/public', tags=['Category API'])


@router.post('/category', status_code=status.HTTP_201_CREATED, response_model=CategoryRead)
def create_category(category: CategoryCreate, session: Session = Depends(get_session)):
    return category_crud.create(category, session)


@router.get('/category', response_model=List[CategoryRead])
# @router.get('/category/with-product', response_model=List[CategoryReadWithProduct])
def read_category(offset: int = 0, limit: int = Query(default=100, lte=100), session: Session = Depends(get_session)):
    return category_crud.get(offset, limit, session)


@router.get('/category/{id}', response_model=CategoryRead)
# @router.get('/category/{id}/with-product', response_model=CategoryReadWithProduct)
def category_by_id(id: int, session: Session = Depends(get_session)):
    return category_crud.get_by_id(id, session)


@router.put('/category/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=CategoryRead)
def category_update(id: int, category: CategoryUpdate, session: Session = Depends(get_session)):
    return category_crud.update(id, category, session)


@router.delete('/category/{id}', response_model=CategoryRead)
def category_delete(id: int, session: Session = Depends(get_session)):
    return category_crud.delete(id, session)
