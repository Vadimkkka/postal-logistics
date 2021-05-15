from datetime import timedelta

from fastapi import APIRouter, Depends, Body, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from dependencies import mail_db
from models.user import User, NewUser

from auth import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_active_user, get_password_hash


router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found user"}},
)


@router.post("/sign-in")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.post("/sign-up")
async def create_user(user: NewUser = Body(...)):
    user = jsonable_encoder(user)
    user['hashed_password'] = get_password_hash(user.pop('password', None))
    new_user = await mail_db["user"].insert_one(user)
    created_user = await mail_db["user"].find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)
