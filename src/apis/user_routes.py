

from typing import List
from fastapi import APIRouter, Depends, Query, status
from sqlmodel import Session
from src.database.database import get_session
from src.models.user.user import User
from src.models.user.user_extended import UserCreate, UserRead, UserUpdate
from src.crud import user_crud

router = APIRouter(tags=['User API', 'V1'])


@router.post('/user', status_code=status.HTTP_201_CREATED, response_model=UserRead)
def create_category(category: UserCreate, session: Session = Depends(get_session)):
    result = user_crud.create(category, session)
    return result


@router.get('/user', response_model=List[UserRead])
def read_category(offset: int = 0, limit: int = Query(default=100, lte=100), session: Session = Depends(get_session)):
    return user_crud.get(offset, limit, session)


@router.get('/user/{id}', response_model=UserRead)
def category_by_id(id: int, session: Session = Depends(get_session)):
    return user_crud.get_by_id(id, session)


@router.put('/user/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=UserRead)
def category_update(id: int, category: UserUpdate, session: Session = Depends(get_session)):
    return user_crud.update(id, category, session)


@router.delete('/user/{id}')
def category_delete(id: int, session: Session = Depends(get_session)):
    return user_crud.delete(id, session)
