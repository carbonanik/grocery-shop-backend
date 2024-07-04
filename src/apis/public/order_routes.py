from typing import List

from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session

from src.database.database import get_session
from src.models.order.order import OrderRead, OrderCreate, OrderUpdate
from src.crud import order_crud

router = APIRouter(prefix='/public', tags=['Order API'])


@router.post('/order', status_code=status.HTTP_201_CREATED, response_model=OrderRead)
def create_order(order: OrderCreate, session: Session = Depends(get_session)):
    return order_crud.create(order, session)


@router.get('/order', response_model=List[OrderRead])
def read_order(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        session: Session = Depends(get_session)
):
    results = order_crud.get(offset, limit, session)
    return results


@router.get('/order/{id}', response_model=OrderRead)
def coupon_by_id(id: int, session: Session = Depends(get_session)):
    return order_crud.get_by_id(id, session)


@router.put('/order/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=OrderRead)
def coupon_update(id: int, order: OrderUpdate, session: Session = Depends(get_session)):
    return order_crud.update(id, order, session)


@router.delete('/order/{id}', status_code=status.HTTP_204_NO_CONTENT)
def coupon_delete(id: int, session: Session = Depends(get_session)):
    return order_crud.delete(id, session)


# @router.post('/order', status_code=status.HTTP_201_CREATED, response_model=OrderRead)
# def create_order(order: OrderCreate, session: Session = Depends(get_session)):

#     def add_items(order: Order):
#         order_items = order.order_items
#         order.order_items = list(map(lambda x: Orderitem.model_validate(x), order_items))

#         coupons = order.coupons
#         order.coupons = list(map(lambda x: session.get(Coupon, x.id), coupons))

#     db_order = order_crud.create_with_items(
#         obj=order,
#         add_items=add_items,
#         session=session
#     )

#     return db_order


# @router.get('/order', response_model=List[OrderRead])
# def read_order(
#         offset: int = 0,
#         limit: int = Query(default=100, lte=100),
#         session: Session = Depends(get_session)
# ):
#     results = order_crud.get(offset, limit, session)
#     return results


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
