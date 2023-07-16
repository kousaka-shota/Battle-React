from fastapi import APIRouter,Depends,HTTPException
from typing import List
from schemas import equipment as equip_schemas
from cruds import equipment as equip_cruds
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/equipments",response_model=List[equip_schemas.Equipment])
async def get_all_equipments(db:Session = Depends(get_db)):
    return equip_cruds.get_all_equipments(db)

# DB登録後、帰ってきてほしい値は全てのデータが入っているschemas,Equipment
@router.post("/equipments",response_model=equip_schemas.Equipment)
# 下の関数実行時、ユーザーはnameとasset_Noしか決めないので、その二つしか持たないクラスを引数とする（CreateEquipment）
async def create_equipment(equipment_body:equip_schemas.CreateEquipment,db:Session = Depends(get_db)):
    # **で辞書を展開し、CreateEquipmentのkeyに割当てている
    new_equip = equip_schemas.CreateEquipment(**equipment_body.dict())
    return equip_cruds.create_equipment(db,new_equip)

@router.delete("/equipments/{equip_id}")
async def delete_equipment(equip_id:int,db:Session = Depends(get_db)):
    return equip_cruds.delete_equipment(db,equip_id)

@router.put("/equipments/{equip_id}",response_model=equip_schemas.Equipment)
async def start_equipment_operation(equip_id:int,db:Session = Depends(get_db)):
    return equip_cruds.start_equipment_operation(db,equip_id)

@router.put("/equipment/{equip_id}",response_model=equip_schemas.Equipment)
async def stop_equipment_operation(equip_id:int,db:Session=Depends(get_db)):
    return equip_cruds.stop_equipment_operation(db,equip_id)

