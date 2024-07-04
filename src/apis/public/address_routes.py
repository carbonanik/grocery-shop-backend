from typing import List

from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session

from src.database.database import get_session
from src.crud import address_crud
from src.models.address.address import *


router = APIRouter(prefix='/public', tags=['Address API'])


@router.post('/address', status_code=status.HTTP_201_CREATED, response_model=AddressRead)
def create_address(address: AddressCreate, session: Session = Depends(get_session)):
    return address_crud.create(address, session)


@router.get('/address', response_model=List[AddressRead])
def read_addresses(
    offset: int = 0, 
    limit: int = Query(default=100, lte=100), 
    session: Session = Depends(get_session)
):
    return address_crud.get(offset, limit, session)


@router.get('/address/{id}', response_model=AddressRead)
def address_by_id(id: int, session: Session = Depends(get_session)):
    return address_crud.get_by_id(id, session)


@router.put('/address/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=AddressRead)
def address_update(id: int, address: AddressUpdate, session: Session = Depends(get_session)):
    return address_crud.update(id, address, session)


@router.delete('/address/{id}', response_model=AddressRead)
def address_delete(id: int, session: Session = Depends(get_session)):
    return address_crud.delete(id, session)
