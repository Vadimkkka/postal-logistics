from fastapi import Depends, FastAPI

from routers import letter
from routers import user

app = FastAPI(debug=True)

app.include_router(letter.router)
app.include_router(user.router)
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
