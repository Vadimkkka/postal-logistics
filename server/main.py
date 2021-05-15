from fastapi import Depends, FastAPI

from routers import letter

app = FastAPI()

app.include_router(letter.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )

@app.get("/")
def read_root():
    return {"Hello": "World"}
