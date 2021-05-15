from pydantic import BaseModel, Field
from typing import Optional

from helpers import PyObjectId, Address
from bson import ObjectId

# from schemes import storehouse_schema


class Storehouse(BaseModel):
    storehouse_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    address: Address

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        # schema_extra = storehouse_schema


class UpdateStorehouse(BaseModel):
    name: str
    address: Optional[Address]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        # schema_extra = storehouse_schema

