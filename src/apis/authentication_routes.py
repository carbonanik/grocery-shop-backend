from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from src.database.database import get_session
from src.deps.auth import ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user, create_access_token, get_current_active_user, get_password_hash
from src.models.user.user import User

from src.crud import user_crud
from src.models.user.user_extended import UserCreate, UserRead, UserUpdate


router = APIRouter(tags=['V1', 'Authentication API'])


@router.post("/token", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserRead)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.post("/register", response_model=UserRead)
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    hashed_password = get_password_hash(user.password)

    db_obj = User.from_orm(
        user,
        {'hashed_password': hashed_password}
    )
    # db_obj.hashed_password = hashed_password

    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


@router.put('/me/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=UserRead)
def update_user(
    id: int,
    update_user: UserUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)
):
    return user_crud.update(id, update_user, session)


@router.delete('/me/{id}')
def delete_user(
    id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)
):
    return user_crud.delete(id, session)
