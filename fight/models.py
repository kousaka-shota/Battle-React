from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


class Equipment(Base):
    __tablename__ ="equipment"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)