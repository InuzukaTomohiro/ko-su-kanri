
from sqlalchemy import Integer, String, Column
from database.base import Base
from pydantic import BaseModel


class TestsTransaction(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)
    test = Column(String(255), nullable=True)
