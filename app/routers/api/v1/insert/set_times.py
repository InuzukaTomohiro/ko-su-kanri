from fastapi import APIRouter

from routers.api.v1.schema.request.set_times import SetTimeRequestModel

router = APIRouter()

@router.post("/set-times")
def set_times(body: SetTimeRequestModel):
    
    set_times = body.start_time
    return {"aaa", "aaaa"}