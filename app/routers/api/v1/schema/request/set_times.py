from pydantic import BaseModel
import datetime
class SetTimeRequestModel(BaseModel):
    """タイマーセット時のリクエストモデル"""
    start_time: datetime.time