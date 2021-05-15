from pydantic import BaseModel, Field
from typing import Optional

from helpers import PyObjectId
from bson import ObjectId

from schemes import user_schema


class User(BaseModel):
    user_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        # schema_extra = user_schema
    
    def hash_password(password: str):
        return "fakehashed" + password



class UserInDB(User):
    hashed_password: str

