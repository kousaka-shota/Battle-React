from fastapi import APIRouter
from typing import List
from schemas import equipment as equip_schemas
from cruds import equipment as equip_cruds

router = APIRouter()

@router.get("/equipments",response_model=List[equip_schemas.Equipment])
async def get_equipments():
    return equip_cruds.get_equipments()

@router.post("/equipments",response_model=equip_schemas.Equipment)
async def create_equipment(equipment_body:equip_schemas.CreateEquipment):
    new_equip = equip_schemas.CreateEquipment(**equipment_body.dict())
    return equip_cruds.create_equipment(new_equip)