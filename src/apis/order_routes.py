from typing import List

from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session, col, select

from src.database.database import get_session
from src.models.coupon.coupon import Coupon
from src.models.order.order import Order
from src.models.order.order_create import OrderCreate
from src.models.order.order_read_with_items import OrderRead
from src.models.order.orderitem import Orderitem
from src.crud import order_crud

router = APIRouter(tags=['Order API', 'V1'])


@router.post('/order', status_code=status.HTTP_201_CREATED, response_model=OrderRead)
def create_order(order: OrderCreate, session: Session = Depends(get_session)):

    def add_items(order: Order):
        order_items = order.order_items
        order.order_items = list(map(lambda x: Orderitem.from_orm(x), order_items))

        coupons = order.coupons
        order.coupons = list(map(lambda x: session.get(Coupon, x.id), coupons))

    db_order = order_crud.create_with_items(
        obj=order,
        add_items=add_items,
        session=session
    )

    return db_order


@router.get('/order', response_model=List[OrderRead])
def read_order(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        session: Session = Depends(get_session)
):
    results = order_crud.get(offset, limit, session)
    return results


# @router.get('/order/{id}', response_model=OrderRead)
# def coupon_by_id(id: int, session: Session = Depends(get_session)):

#     order = session.get(Order, id)
#     if not order:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail='Order not found')
#     return order


# @router.put('/order/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=OrderRead)
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


# @router.delete('/order/{id}')
# def order_delete(id: int, session: Session = Depends(get_session)):
#     order = session.get(Order, id)
#     if not order:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
#     session.delete(order)
#     session.commit()
#     return {"ok": True}
