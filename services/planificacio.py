from schema.planificacions_sch import planificacions_schema
from sqlmodel import Session, select
from models.Planificacio import Planificacio

#-----------------------------taula-Planificacio------------------------------------------------#
def get_all_planificacions(db: Session):
    sql_read = select(Planificacio)
    planificacions = db.exec(sql_read).all()
    return planificacions_schema(planificacions)

def get_planificacio(id_horari: int, db: Session):
    sql_read = select(Planificacio).where(Planificacio.id_horari == id_horari)
    planificacio = db.exec(sql_read).one()
    return planificacio.dict()

def add_new_planificacio(
    id_horari: int,
    data: str,
    horari: str,
    rol: str,
    id_empleat: int,
    db: Session
):
    db_planificacio = Planificacio(
        id_horari=id_horari,
        data=data,
        horari=horari,
        rol=rol,
        id_empleat=id_empleat
    )
    db.add(db_planificacio)
    db.commit()
    db.refresh(db_planificacio)
    return {"Missatge": "Planificació creada correctament"}

def update_planificacio(
    id_horari: int,
    data: str,
    horari: str,
    rol: str,
    id_empleat: int,
    db: Session
):
    sql_select = select(Planificacio).where(Planificacio.id_horari == id_horari)
    planificacio_db = db.exec(sql_select).one()

    planificacio_db.data = data
    planificacio_db.horari = horari
    planificacio_db.rol = rol
    planificacio_db.id_empleat = id_empleat

    db.add(planificacio_db)
    db.commit()
    db.refresh(planificacio_db)
    return {"Missatge": "Planificació actualitzada correctament"}

def update_planificacio_field(id_horari: int, data: dict, db: Session):
    sql_select = select(Planificacio).where(Planificacio.id_horari == id_horari)
    planificacio_db = db.exec(sql_select).one_or_none()

    if not planificacio_db:
        return None

    for key, value in data.items():
        if hasattr(planificacio_db, key) and key != "id_horari":
            setattr(planificacio_db, key, value)

    db.add(planificacio_db)
    db.commit()
    db.refresh(planificacio_db)
    return {"Missatge": "Camp(s) de la planificació actualitzat(s) correctament"}

def delete_planificacio(id_horari: int, db: Session):
    sql_select = select(Planificacio).where(Planificacio.id_horari == id_horari)
    planificacio_db = db.exec(sql_select).one()

    db.delete(planificacio_db)
    db.commit()
    return {"Missatge": "Planificació esborrada correctament"}
#---------------------------final-taula-Planificacio----------------------------------------------#
