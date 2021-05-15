from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from helpers import PyObjectId
from bson import ObjectId

from schemes import user_schema, new_user_schema


class Role(str, Enum):
    user = "user"
    expert = "expert"
    admin = "admin"


class User(BaseModel):
    user_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    full_name: Optional[str] = None
    role: Role
    disabled: Optional[bool] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = user_schema


class UserInDB(User):
    hashed_password: str

class NewUser(User):
    password: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = { ObjectId: str }
        schema_extra = new_user_schema
