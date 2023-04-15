from typing import Type, TypeVar
from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlmodel import SQLModel, Session, col, select


ModelType = TypeVar('ModelType', bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class BaseCRUD():

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(
        self,
        obj: CreateSchemaType,
        session: Session
    ) -> ModelType:
        db_obj = self.model.from_orm(obj)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj
    
    def create_with_items(
        self,
        obj: CreateSchemaType,
        add_items,
        session: Session
    ) -> ModelType:
        db_obj = self.model.from_orm(obj)

        db_obj = add_items(db_obj)

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def get(
        self,
        offset: int,
        limit: int,
        session: Session
    ) -> ModelType:
        return session.exec(
            select(self.model)
            .offset(offset)
            .limit(limit)
        ).all()

    def get_by_id(
        self,
        id: int,
        session: Session
    ) -> ModelType:
        db_obj = session.get(self.model, id)
        print(self.model.__name__)
        if not db_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'{self.model.__name__} not found')
        return db_obj

    def get_by_ids(
        self,
        ids: list[int],
        session: Session
    ) -> ModelType:
        return session.exec(
            select(self.model)
            .where(col(self.model.id).in_(ids))
        ).all()

    def update(
        self,
        id: int,
        entity,
        session: Session
    ) -> ModelType:
        db_obj = session.get(self.model, id)

        if not db_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'{self.model.__name__} not found'
            )

        obj_data = entity.dict(exclude_unset=True)
        for key, value in obj_data.items():
            setattr(db_obj, key, value)

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def delete(entity_type: Type[ModelType], id: int, session: Session):
        db_entity = session.get(entity_type, id)
        if not db_entity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'{entity_type.__name__} not found'
            )
        session.delete(db_entity)
        session.commit()
        return db_entity

