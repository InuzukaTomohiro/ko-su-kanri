"""apiルーティング"""

from fastapi import APIRouter

from routers.api import v1

router = APIRouter()
router.include_router(
    router=v1.router,
    prefix="/v1"
)