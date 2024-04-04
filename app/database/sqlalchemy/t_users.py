from sqlalchemy import BigInteger, String, Column, Boolean, DateTime
from database.base import Base
from pydantic import BaseModel
from datetime import datetime


class TWorkRecordsTransaction(Base):
    __tablename__ = "t_users"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    deleted_flag = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now, nulable=False)
    updated_at = Column(DateTime, default=datetime.now, nulable=False)
    deleted_at = Column(DateTime, nulable=True)
    
