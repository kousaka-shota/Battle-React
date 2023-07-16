import models
from datetime import datetime
from sqlalchemy.orm import Session
from schemas import sensor as sensor_schema

def get_all_sensor(db:Session):
    return db.query(models.Sensor).all()

def create_sensor(db:Session,new_sensor:sensor_schema.CreateSensor):
    db_sensor = models.Sensor(name=new_sensor.name,equip_id=new_sensor.equip_id)
    print(f"{db_sensor.equip_id}と{db_sensor.name}")
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor