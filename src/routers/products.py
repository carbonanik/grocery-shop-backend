from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlmodel import Session, select

from database.database import get_session
from models.product import *
from models.product_and_category import ProductReadWithCategory

router = APIRouter()


@router.post('/product', status_code=status.HTTP_201_CREATED, response_model=ProductRead)
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    db_product = Product.from_orm(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@router.get('/product', response_model=List[ProductRead])
@router.get('/product/with-category', response_model=List[ProductReadWithCategory])
def read_products(
        offset: int = 0, limit: int = Query(default=100, lte=100), session: Session = Depends(get_session)
):
    results = session.exec(select(Product).offset(offset).limit(limit)).all()
    return results


@router.post('/product/favorite', response_model=List[ProductRead])
def favorite_product(ids: List[int], session: Session = Depends(get_session)):
    result = session.execute(f'SELECT * FROM product WHERE id IN {tuple(ids)}').fetchall()
    return result


@router.get('/product/{id}', response_model=ProductRead)
@router.get('/product/{id}/with-category', response_model=ProductReadWithCategory)
def product_by_id(id: int, session: Session = Depends(get_session)):
    
    product = session.get(Product, id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    return product


@router.put('/product/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=ProductRead)
def product_update(id: int, product: ProductUpdate, session: Session = Depends(get_session)):
    db_product = session.get(Product, id)

    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    product_data = product.dict(exclude_unset=True)
    for key, value in product_data.items():
        setattr(db_product, key, value)

    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@router.delete('/product/{id}')
def product_delete(id: int, session: Session = Depends(get_session)):
    hero = session.get(Product, id)
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}
