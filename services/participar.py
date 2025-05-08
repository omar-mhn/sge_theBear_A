from schema.participar_sch import participacions_schema
from sqlmodel import Session, select
from models.Participar import Participar

#--------------------------------taula-Participar---------------------------------------------------#
def get_all_participacions(db: Session):
    sql_read = select(Participar)
    participacions = db.exec(sql_read).all()
    return participacions_schema(participacions)

def get_participacio(id_empleat: int, id_reunio: int, id_proveidor: int, db: Session):
    sql_read = select(Participar).where(
        Participar.id_empleat == id_empleat,
        Participar.id_reunio == id_reunio,
        Participar.id_proveidor == id_proveidor
    )
    participacio = db.exec(sql_read).one()
    return participacio.dict()

def add_new_participacio(id_empleat: int, id_reunio: int, id_proveidor: int, db: Session):
    db_participacio = Participar(
        id_empleat=id_empleat,
        id_reunio=id_reunio,
        id_proveidor=id_proveidor
    )
    db.add(db_participacio)
    db.commit()
    db.refresh(db_participacio)
    return {"Missatge": "Participació creada correctament"}

def delete_participacio(id_empleat: int, id_reunio: int, id_proveidor: int, db: Session):
    sql_select = select(Participar).where(
        Participar.id_empleat == id_empleat,
        Participar.id_reunio == id_reunio,
        Participar.id_proveidor == id_proveidor
    )
    participacio_db = db.exec(sql_select).one()

    db.delete(participacio_db)
    db.commit()
    return {"Missatge": "Participació esborrada correctament"}
#-----------------------------final-taula-Participar------------------------------------------------#