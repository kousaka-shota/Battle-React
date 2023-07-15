from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from datetime import datetime

class Equipment(Base):
    __tablename__ ="equipment"
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    name = Column(String(10))
    asset_No = Column(String(8))
    create_date = Column(DateTime,default=datetime.now())