from typing import List

from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session, select

from src.database.database import get_session
from src.models.coupon import Coupon
from src.models.order import Order
from src.models.order_create import OrderCreate
from src.models.order_with_items import OrderRead

router = APIRouter()


@router.post('/order', status_code=status.HTTP_201_CREATED, response_model=OrderRead, tags=['Order API'])
def create_order(order: OrderCreate, session: Session = Depends(get_session)):

    order_items = order.order_items
    coupons = order.coupons

    db_order = Order.from_orm(order)
    db_order.order_items = order_items
    
    db_order.coupons = list(map(lambda x: session.get(Coupon, x.id), coupons))

    session.add(db_order)
    session.commit()
    session.refresh(db_order)

    return db_order


@router.get('/order', response_model=List[OrderRead], tags=['Order API'])
def read_order(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        session: Session = Depends(get_session)
):
    results = session.exec(select(Order).offset(offset).limit(limit)).all()
    return results


# @router.get('/order/{id}', response_model=OrderRead, tags=['Order API'])
# def coupon_by_id(id: int, session: Session = Depends(get_session)):

#     order = session.get(Order, id)
#     if not order:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail='Order not found')
#     return order


# @router.put('/order/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=OrderRead, tags=['Order API'])
# def order_update(id: int, order: OrderUpdate, session: Session = Depends(get_session)):
#     db_order = session.get(Order, id)

#     if not db_order:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

#     order_data = order.dict(exclude_unset=True)
#     for key, value in order_data.items():
#         setattr(db_order, key, value)

#     session.add(db_order)
#     session.commit()
#     session.refresh(db_order)
#     return db_order


# @router.delete('/order/{id}', tags=['Order API'])
# def order_delete(id: int, session: Session = Depends(get_session)):
#     order = session.get(Order, id)
#     if not order:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
#     session.delete(order)
#     session.commit()
#     return {"ok": True}
