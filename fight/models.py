from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime,Boolean
from datetime import datetime
from sqlalchemy.orm import relationship
from cruds import equipment as cruds_equip

class Equipment(Base):
    __tablename__ ="equipment"
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    name = Column(String(10))
    asset_No = Column(String(8),unique=True)
    create_date = Column(DateTime,default=datetime.now())
    operation = Column(Boolean,default=False)

    sensor = relationship("Sensor",back_populates="equipment")

class Sensor(Base):
    __tablename__ = "sensor"
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    name = Column(String(10))
    equip_id = Column(Integer,ForeignKey("equipment.id"))
    operation = Column(Boolean,default=False)

    equipment = relationship("Equipment",back_populates="sensor")
