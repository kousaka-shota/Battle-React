from schemas import equipment as equip_schemas
import models

equipments=[
    {
        "id":1,
        "name":"試験機1"
    },
    {
        "id":2,
        "name":"試験機2"
    }
]

def get_equipments():
    return equipments

def create_equipment(new_equip:equip_schemas.CreateEquipment):
    #本来、idに関する操作は不要（DBが勝手にincrementしてくれる）
    id = len(equipments) + 1
    db_equip = models.Equipment(id =id,name=new_equip.name)
    equipments.append({
        "id":db_equip.id,
        "name":db_equip.name
    })
    print(equipments)
    return db_equip