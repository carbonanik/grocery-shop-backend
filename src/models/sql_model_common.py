from sqlmodel import Field, SQLModel
from datetime import datetime


class SQLModelCommon(SQLModel):
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    deleted_at: datetime | None = Field(default=None, nullable=True)