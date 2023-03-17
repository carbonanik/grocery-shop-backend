from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlmodel import Session, select

from src.database.database import get_session
from src.models.coupon import CouponRead, Coupon, CouponCreate, CouponUpdate

router = APIRouter()


@router.post('/coupon', status_code=status.HTTP_201_CREATED, response_model=CouponRead, tags=['Coupon API'])
def create_coupon(coupon: CouponCreate, session: Session = Depends(get_session)):
    db_coupon = Coupon.from_orm(coupon)
    session.add(db_coupon)
    session.commit()
    session.refresh(db_coupon)
    return db_coupon


@router.get('/coupon', response_model=List[CouponRead], tags=['Coupon API'])
def read_coupon(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        session: Session = Depends(get_session)
):
    results = session.exec(select(Coupon).offset(offset).limit(limit)).all()
    return results


# @router.get('/coupon/{id}', response_model=CouponRead, tags=['Coupon API'])
# def coupon_by_id(id: int, session: Session = Depends(get_session)):

#     coupon = session.get(Coupon, id)
#     if not coupon:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail='Coupon not found')
#     return coupon


# @router.put('/coupon/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=CouponRead, tags=['Coupon API'])
# def coupon_update(id: int, coupon: CouponUpdate, session: Session = Depends(get_session)):
#     db_coupon = session.get(Coupon, id)

#     if not db_coupon:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Coupon not found")

#     coupon_data = coupon.dict(exclude_unset=True)
#     for key, value in coupon_data.items():
#         setattr(db_coupon, key, value)

#     session.add(db_coupon)
#     session.commit()
#     session.refresh(db_coupon)
#     return db_coupon


# @router.delete('/coupon/{id}', tags=['Coupon API'])
# def coupon_delete(id: int, session: Session = Depends(get_session)):
#     coupon = session.get(Coupon, id)
#     if not coupon:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Coupon not found")
#     session.delete(coupon)
#     session.commit()
#     return {"ok": True}
