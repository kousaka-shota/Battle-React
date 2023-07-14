from pydantic import BaseModel,Field

class CreateEquipment(BaseModel):
    name:str = Field(None,max_length=10)

class Equipment(CreateEquipment):
    id:int

    class Config:
        orm_mode = True
    