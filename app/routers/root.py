from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    """ルート"""
    return {"message": "工数管理アップのルートです。"}