from sqlmodel import Field

from src.models.sql_model_common import SQLModelCommon


class AddressBase(SQLModelCommon):
    address_line_1: str | None = None
    address_line_2: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    postcode: str | None = None


class Address(AddressBase, table=True):
    __table_args__ = {'extend_existing': True}

    id: int | None = Field(default=None, primary_key=True)


class AddressUpdate(AddressBase):
    pass


class AddressCreate(AddressBase):
    pass


class AddressRead(AddressBase):
    id: int
