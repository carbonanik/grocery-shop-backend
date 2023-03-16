from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlmodel import Session, select

from src.database.database import get_session
from src.models.category import *
from src.models.product_and_category import CategoryReadWithProduct

router = APIRouter()


@router.post('/category', status_code=status.HTTP_201_CREATED, response_model=CategoryRead)
def create_category(category: CategoryCreate, session: Session = Depends(get_session)):
    db_category = Category.from_orm(category)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category


@router.get('/category', response_model=List[CategoryRead])
@router.get('/category/with-product', response_model=List[CategoryReadWithProduct])
def read_category(offset: int = 0, limit: int = Query(default=100, lte=100), session: Session = Depends(get_session)):
    results = session.exec(select(Category).offset(offset).limit(limit)).all()
    return results


@router.get('/category/{id}', response_model=CategoryRead)
@router.get('/category/{id}/with-product', response_model=CategoryReadWithProduct)
def category_by_id(id: int, session: Session = Depends(get_session)):
    category = session.get(Category, id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Product not found')
    return category


@router.put('/category/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=CategoryRead)
def category_update(id: int, product: CategoryUpdate, session: Session = Depends(get_session)):
    db_category = session.get(Category, id)

    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    category_data = product.dict(exclude_unset=True)
    for key, value in category_data.items():
        setattr(db_category, key, value)

    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category


@router.delete('/category/{id}')
def category_delete(id: int, session: Session = Depends(get_session)):
    category = session.get(Category, id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    session.delete(category)
    session.commit()
    return {"ok": True}
