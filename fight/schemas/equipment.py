from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional

class CreateEquipment(BaseModel):
    # Optionalは値が入ってなくてもOK
    name:Optional[str] = Field(None,max_length=10)
    asset_No:Optional[str] = Field(None,max_length=8)

class Equipment(CreateEquipment):
    id:int
    create_date:datetime = Field(datetime.now())
    operation:bool= Field(False)

    class Config:
        orm_mode = True
    