from fastapi import APIRouter,Depends,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from schemas import sensor as sensor_schema
from cruds import sensor as sensor_crud
from cruds import equipment as equip_crud

from typing import List

router = APIRouter()

@router.get("/sensor",response_model=List[sensor_schema.Sensor])
async def get_all_sensor(db:Session = Depends(get_db)):
    return sensor_crud.get_all_sensor(db)

@router.post("/sensor",response_model=sensor_schema.Sensor)
async def create_sensor(db:Session = Depends(get_db),sensor_body:sensor_schema.CreateSensor=None):
    new_sensor = sensor_schema.CreateSensor(**sensor_body.dict())
    validate_to_equip_id(new_sensor.equip_id,db)
    return sensor_crud.create_sensor(db,new_sensor)

def validate_to_equip_id(equip_id:int,db:Session=Depends(get_db)):
    vali_equip = equip_crud.get_equipment(db,equip_id)
    if vali_equip is None:
        raise HTTPException(status_code=404,detail="equipment is not found") 
    return