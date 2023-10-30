from fastapi import APIRouter

from routers.api.v1.insert import set_times

router = APIRouter()

router.include_router(
    router=set_times.router,
    prefix=""
)