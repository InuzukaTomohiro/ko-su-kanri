
from sqlalchemy import BigInteger, String, Column, Text, DateTime, Boolean
from sqlalchemy.schema import ForeignKey
from database.base import Base
from pydantic import BaseModel
from datetime import datetime


class TWorkRecordsTransaction(Base):
    __tablename__ = "t_work_records"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("t_users.id", name="fk_t_user_id", nullable=False))
    work_type = Column(BigInteger, ForeignKey("m_work_types.id", name="fk_m_work_type_id", nullable=True))
    user_work_type = Column(BigInteger, ForeignKey("t_user_work_types.id", name="t_user_work_type_id", nullable=True))
    work_name = Column(String(255), nullable=False),
    work_description = Column(Text(), nullable=True),
    started_at = Column(DateTime(), default=datetime.now, nullable=False),
    finished_at = Column(DateTime(), nullable=True)    
    deleted_flag = Column(Boolean, default=datetime.now, nullable=False)
    created_at = Column(DateTime(), )
