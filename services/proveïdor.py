from schema.proveïdors_sch import proveïdors_schema
from sqlmodel import Session, select
from models.Proveïdor import Proveïdor

#--------------------------------taula-Proveïdor---------------------------------------------------#

def get_all_proveïdors(db: Session):
    sql_read = select(Proveïdor)
    proveïdors = db.exec(sql_read).all()
    return proveïdors_schema(proveïdors)

def get_proveïdor(id_proveïdor: int, db: Session):
    sql_read = select(Proveïdor).where(Proveïdor.id_proveïdor == id_proveïdor)
    proveïdor = db.exec(sql_read).one()
    return proveïdor.dict()

def add_new_proveïdor(id_proveïdor: int, Nom: str, telefòn: str, email: str, informaciò: str, db: Session):
    db_proveïdor = Proveïdor(
        id_proveïdor=id_proveïdor,
        Nom=Nom,
        telefòn=telefòn,
        email=email,
        informaciò=informaciò
    )
    db.add(db_proveïdor)
    db.commit()
    db.refresh(db_proveïdor)
    return {"Missatge": "Proveïdor creat correctament"}

def update_proveïdor(
    id_proveïdor: int,
    Nom: str,
    telefòn: str,
    email: str,
    informaciò: str,
    db: Session
):
    sql_select = select(Proveïdor).where(Proveïdor.id_proveïdor == id_proveïdor)
    proveïdor_db = db.exec(sql_select).one()

    proveïdor_db.Nom = Nom
    proveïdor_db.telefòn = telefòn
    proveïdor_db.email = email
    proveïdor_db.informaciò = informaciò

    db.add(proveïdor_db)
    db.commit()
    db.refresh(proveïdor_db)
    return {"Missatge": "Proveïdor actualitzat correctament"}

def update_proveïdor_field(id_proveïdor: int, data: dict, db: Session):
    sql_select = select(Proveïdor).where(Proveïdor.id_proveïdor == id_proveïdor)
    proveïdor_db = db.exec(sql_select).one_or_none()

    if not proveïdor_db:
        return None

    for key, value in data.items():
        if hasattr(proveïdor_db, key) and key != "id_proveïdor":
            setattr(proveïdor_db, key, value)

    db.add(proveïdor_db)
    db.commit()
    db.refresh(proveïdor_db)
    return {"Missatge": "Camp(s) de la proveïdor actualitzat(s) correctament"}

def delete_proveïdor(id_proveïdor: int, db: Session):
    sql_select = select(Proveïdor).where(Proveïdor.id_proveïdor == id_proveïdor)
    proveïdor_db = db.exec(sql_select).one()

    db.delete(proveïdor_db)
    db.commit()
    return {"Missatge": "Proveïdor esborrat correctament"}

#-----------------------------final-taula-Proveïdor------------------------------------------------#