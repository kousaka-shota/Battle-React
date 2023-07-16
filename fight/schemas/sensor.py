from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional

class CreateSensor(BaseModel):
    name:Optional[str] = Field(None,max_length=10)
    equip_id:int 

class Sensor(CreateSensor):
    id:int
    operation:bool = Field(False)

    class Config:
        orm_mode = True
    