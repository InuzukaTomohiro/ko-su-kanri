from fastapi import APIRouter

from routers.api.v1 import read, insert

router = APIRouter()

router.include_router(
    router=read.router,
    prefix="/read"
)

router.include_router(
    router=insert.router,
    prefix="/insert"
)