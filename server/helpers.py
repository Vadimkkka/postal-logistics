from pydantic import BaseModel
from typing import Optional

from bson import ObjectId
# from amzqr import amzqr

# def create_qrcode(name, url):
#     return amzqr.run(
#         url,
#         version=4,
#         level='H',
#         picture='postbox.png',
#         colorized=True,
#         contrast=1.0,
#         brightness=1.0,
#         # save_name=name,
#         # save_dir=os.getcwd()
#     )

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


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

