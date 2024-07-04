from typing import List

from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session

from src.database.database import get_session
from src.models.coupon.coupon import *
from src.crud import coupon_crud


router = APIRouter(prefix='/public', tags=['Coupon API'])


@router.post('/coupon', status_code=status.HTTP_201_CREATED, response_model=CouponRead)
def create_coupon(coupon: CouponCreate, session: Session = Depends(get_session)):
    return coupon_crud.create(coupon, session)
    


@router.get('/coupon', response_model=List[CouponRead])
def read_coupon(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        session: Session = Depends(get_session)
):
    return coupon_crud.get(offset, limit, session)
    


@router.get('/coupon/{id}', response_model=CouponRead)
def coupon_by_id(id: int, session: Session = Depends(get_session)):
    return coupon_crud.get_by_id(id, session)


@router.put('/coupon/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=CouponRead)
def coupon_update(id: int, coupon: CouponUpdate, session: Session = Depends(get_session)):
    return coupon_crud.update(id, coupon, session)


@router.delete('/coupon/{id}')
def coupon_delete(id: int, session: Session = Depends(get_session)):
    return coupon_crud.delete(id, session)
