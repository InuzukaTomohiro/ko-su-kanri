from fastapi import APIRouter

from routers.api.v1.schema.request.set_times import SetTimeRequestModel
from database.sqlalchemy.tests import TestsTransaction
from settings.database import SessionLocal
from sqlalchemy import select

router = APIRouter()

@router.post("/set-times")
def set_times(test: int):
    with SessionLocal.begin() as session:
        # test = session.scalars((
        #         select(TestsTransaction)
        #     )
        # ).all()
        test = session.query(TestsTransaction).first()
        print("@@@@@@@@@@@@", test.test)
    
  
    return {"data": test}
    
    