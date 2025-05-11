from schema.proveidors_sch import proveidors_schema
from sqlmodel import Session, select
from models.Proveidor import Proveidor

#--------------------------------taula-Proveïdor---------------------------------------------------#

def get_all_proveidors(db: Session):
    sql_read = select(Proveidor)
    proveidors = db.exec(sql_read).all()
    return proveidors_schema(proveidors)

def get_proveidor(id_proveidor: int, db: Session):
    sql_read = select(Proveidor).where(Proveidor.id_proveidor == id_proveidor)
    proveidor = db.exec(sql_read).one()
    return proveidor.dict()

def add_new_proveidor(id_proveidor: int, Nom: str, telefòn: str, email: str, informaciò: str, db: Session):
    db_proveidor = Proveidor(
        id_proveidor=id_proveidor,
        Nom=Nom,
        telefòn=telefòn,
        email=email,
        informaciò=informaciò
    )
    db.add(db_proveidor)
    db.commit()
    db.refresh(db_proveidor)
    return {"Missatge": "Proveidor creat correctament"}

def update_proveidor(
    id_proveidor: int,
    Nom: str,
    telefòn: str,
    email: str,
    informaciò: str,
    db: Session
):
    sql_select = select(Proveidor).where(Proveidor.id_proveidor == id_proveidor)
    proveidor_db = db.exec(sql_select).one()

    proveidor_db.Nom = Nom
    proveidor_db.telefòn = telefòn
    proveidor_db.email = email
    proveidor_db.informaciò = informaciò

    db.add(proveidor_db)
    db.commit()
    db.refresh(proveidor_db)
    return {"Missatge": "Proveidor actualitzat correctament"}

def update_proveidor_field(id_proveidor: int, data: dict, db: Session):
    sql_select = select(Proveidor).where(Proveidor.id_proveidor == id_proveidor)
    proveidor_db = db.exec(sql_select).one_or_none()

    if not proveidor_db:
        return None

    for key, value in data.items():
        if hasattr(proveidor_db, key) and key != "id_proveidor":
            setattr(proveidor_db, key, value)

    db.add(proveidor_db)
    db.commit()
    db.refresh(proveidor_db)
    return {"Missatge": "Camp(s) de la proveidor actualitzat(s) correctament"}

def delete_proveidor(id_proveidor: int, db: Session):
    sql_select = select(Proveidor).where(Proveidor.id_proveidor == id_proveidor)
    proveidor_db = db.exec(sql_select).one()

    db.delete(proveidor_db)
    db.commit()
    return {"Missatge": "Proveidor esborrat correctament"}

#-----------------------------final-taula-Proveidor------------------------------------------------#