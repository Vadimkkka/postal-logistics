from fastapi import APIRouter, Depends, Body, status, HTTPException
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder

from typing import List

from models.letter import Letter, UpdateLetter

from dependencies import mail_db

# from io import StringIO
# from bson.binary import Binary
# import base64

router = APIRouter(
    prefix="/letters",
    tags=["Letters"],
    responses={404: {"description": "Not found letter"}},
)


@router.get("/", response_description="List all letters", response_model=List[Letter])
async def list_letters():
    letters = await mail_db['letter'].find().to_list(100)
    return letters


@router.post("/", response_description="Add new letter", response_model=Letter)
async def create_letter(letter: Letter = Body(...)):
    letter = jsonable_encoder(letter)
    # qrcode = create_qrcode(letter['_id'], letter['_id'])
    # with open("./postbox_qrcode.png", "rb") as f:
    #     encoded = Binary(f.read())
    # letter['qrcode'] = jsonable_encoder(base64.b64encode(encoded))
    new_letter = await mail_db["letter"].insert_one(letter)
    created_letter = await mail_db["letter"].find_one({"_id": new_letter.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_letter)


@router.get("/{letter_id}", response_description="Get a single letter", response_model=Letter)
async def read_letter(letter_id: str):
    if (letter := await mail_db["letter"].find_one({"_id": letter_id})) is not None:
        return letter
    raise HTTPException(status_code=404, detail=f"Letter {id} not found")


@router.put("/{letter_id}", response_description="Update a letter", response_model=Letter)
async def update_letter(letter_id: str, letter: UpdateLetter = Body(...)):
    letter = {k: v for k, v in letter.dict().items() if v is not None}

    if len(letter) >= 1:
        update_result = await mail_db["letter"].update_one({"_id": letter_id}, {"$set": letter})

        if update_result.modified_count == 1:
            if (
                updated_letter := await mail_db["letter"].find_one({"_id": letter_id})
            ) is not None:
                return updated_letter

    if (existing_letter := await mail_db["letter"].find_one({"_id": letter_id})) is not None:
        return existing_letter

    raise HTTPException(status_code=404, detail=f"Letter {id} not found")


@router.delete("/{letter_id}", response_description="Delete a letter")
async def delete_letter(letter_id: str):
    delete_result = await mail_db["letter"].delete_one({"_id": letter_id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Letter {id} not found")


@router.delete("/", response_description="Delete all letters")
async def drop_letters():
    delete_result = await mail_db["letter"].drop()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
