from fastapi import APIRouter

router = APIRouter()

@router.post("/set-times")
def set_times(body: SetTimesRequestModel):
    return