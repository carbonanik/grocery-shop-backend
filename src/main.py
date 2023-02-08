from typing import List

import uvicorn as uv
from fastapi import FastAPI, Depends, status, HTTPException, Query
from sqlmodel import Session, select
from fastapi.middleware.cors import CORSMiddleware

from src.database.database import create_db_and_tables, get_session
from src.models.product import *

app = FastAPI(debug=True)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post('/product', status_code=status.HTTP_201_CREATED, response_model=ProductRead)
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    db_product = Product.from_orm(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@app.get('/product', response_model=List[ProductRead])
def read_products(offset: int = 0, limit: int = Query(default=100, lte=100), session: Session = Depends(get_session)):
    results = session.exec(select(Product).offset(offset).limit(limit)).all()

    return results


@app.get('/product/{id}', response_model=ProductRead)
def product_by_id(id: int, session: Session = Depends(get_session)):
    product = session.get(Product, id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Product not found')
    return product


@app.put('/product/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=ProductRead)
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


@app.delete('/product/{id}')
def product_delete(id: int, session: Session = Depends(get_session)):
    hero = session.get(Product, id)
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}


if __name__ == "__main__":
    uv.run("main:app", port=8000, log_level="info", reload=True)

# photo base url
# https://test-and-devops-environment.s3.amazonaws.com/photos/
