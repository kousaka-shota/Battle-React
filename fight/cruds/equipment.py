from schemas import equipment as equip_schemas
import models
from datetime import datetime
from sqlalchemy.orm import Session

equipments=[
    {
        "id":1,
        "name":"試験機1",
        "asset_No":"11111111",
        "create_date":datetime.now()
    },
    {
        "id":2,
        "name":"試験機2",
        "asset_No":"11111111",
        "create_date":datetime.now()
    }
]

def get_all_equipments(db:Session):
    return db.query(models.Equipment).all()

def get_equipment(db:Session,equip_id:int):
    return db.query(models.Equipment).filter(models.Equipment.id == equip_id).first()

def create_equipment(db:Session,new_equip:equip_schemas.CreateEquipment):
    #本来、idに関する操作は不要（DBが勝手にincrementしてくれる）
    id = len(equipments) + 1

    # DBに保存する際に本当はmodelsのように初期値をセットしてくれるらしいから29行目のやつでいい
    # db_equip = models.Equipment(id =id,name=new_equip.name,asset_No=new_equip.asset_No,create_date=datetime.now())
    db_equip = models.Equipment(name=new_equip.name,asset_No=new_equip.asset_No)
    # equipments.append({
    #     "id":db_equip.id,
    #     "name":db_equip.name,
    #     "asset_No":db_equip.asset_No,
    #     "create_date":db_equip.create_date
    # })
    # print(equipments)

    db.add(db_equip)
    db.commit()
    db.refresh(db_equip)
    return db_equip

def delete_equipment(db:Session,equip_id:int):
    # idからequipmentを取得
    del_equipment = get_equipment(db,equip_id)
    # 取得したequipmentを削除する
    if del_equipment is not None:
        db.delete(del_equipment)
        db.commit()
    return del_equipment