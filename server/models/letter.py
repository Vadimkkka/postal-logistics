from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from helpers import PyObjectId
from bson import ObjectId

from schemes import letter_schema


class Recipient(BaseModel):
    first: str
    last: str
    middle: str

class Address(BaseModel):
    country: str
    city: str
    district: Optional[str] = None
    street: str
    house_number: str
    postcode: str

class Status(str, Enum):
    pending = "Pending"
    in_way = "In way"
    on_storehouse = "On storehouse"
    progress = "In progress"
    delivered = "Delivered"
    canceled = "Canceled"


class Letter(BaseModel):
    letter_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    recipient: Recipient
    address: Address
    track: bool
    status: Optional[Status] = None
    express: bool

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = letter_schema


class UpdateLetter(BaseModel):
    recipient: Optional[Recipient]
    address: Optional[Address]
    track: Optional[bool]
    express: Optional[bool]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = letter_schema
