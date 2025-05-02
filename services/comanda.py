from schema.comandes_sch import comandes_schema
from sqlmodel import Session, select
from models.Comanda import Comanda

#--------------------------------taula-Comanda---------------------------------------------------#
def get_all_comandes(db: Session):
    sql_read = select(Comanda)
    comandes = db.exec(sql_read).all()
    return comandes_schema(comandes)

def get_comanda(id_comanda: int, db: Session):
    sql_read = select(Comanda).where(Comanda.id_comanda == id_comanda)
    comanda = db.exec(sql_read).one()
    return comanda.dict()

def add_new_comanda(id_comanda: int, n_taula: int, quantitat: int, producte: str, data: str, id_client: int, db: Session):
    db_comanda = Comanda(
        id_comanda=id_comanda,
        n_taula=n_taula,
        quantitat=quantitat,
        producte=producte,
        data=data,
        id_client=id_client
    )
    db.add(db_comanda)
    db.commit()
    db.refresh(db_comanda)
    return {"Missatge": "Comanda creada correctament"}

def update_comanda(
    id_comanda: int,
    n_taula: int,
    quantitat: int,
    producte: str,
    data: str,
    id_client: int,
    db: Session
):
    sql_select = select(Comanda).where(Comanda.id_comanda == id_comanda)
    comanda_db = db.exec(sql_select).one()

    comanda_db.n_taula = n_taula
    comanda_db.quantitat = quantitat
    comanda_db.producte = producte
    comanda_db.data = data
    comanda_db.id_client = id_client

    db.add(comanda_db)
    db.commit()
    db.refresh(comanda_db)
    return {"Missatge": "Comanda actualitzada correctament"}

def update_comanda_field(id_comanda: int, data: dict, db: Session):
    sql_select = select(Comanda).where(Comanda.id_comanda == id_comanda)
    comanda_db = db.exec(sql_select).one_or_none()

    if not comanda_db:
        return None

    for key, value in data.items():
        if hasattr(comanda_db, key) and key != "id_comanda":
            setattr(comanda_db, key, value)

    db.add(comanda_db)
    db.commit()
    db.refresh(comanda_db)
    return {"Missatge": "Camp(s) de la comanda actualitzat(s) correctament"}

def delete_comanda(id_comanda: int, db: Session):
    sql_select = select(Comanda).where(Comanda.id_comanda == id_comanda)
    comanda_db = db.exec(sql_select).one()

    db.delete(comanda_db)
    db.commit()
    return {"Missatge": "Comanda esborrada correctament"}
#-----------------------------final-taula-Comanda------------------------------------------------#