from schema.compres_sch import compres_schema
from sqlmodel import Session, select
from models.Compra import Compra

#--------------------------------taula-Compra---------------------------------------------------#
def get_all_compres(db: Session):
    sql_read = select(Compra)
    compres = db.exec(sql_read).all()
    return compres_schema(compres)

def get_compra(id_compra: int, db: Session):
    sql_read = select(Compra).where(Compra.id_compra == id_compra)
    compra = db.exec(sql_read).one()
    return compra.dict()

def add_new_compra(
    id_compra: int,
    proveïdor: str,
    productes: str,
    quantitat_producte: int,
    preu_producte: int,
    preu_total: int,
    data_compra: str,
    db: Session
    ):
    db_compra = Compra(
        id_compra=id_compra,
        proveïdor=proveïdor,
        productes=productes,
        quantitat_producte=quantitat_producte,
        preu_producte=preu_producte,
        preu_total=preu_total,
        data_compra=data_compra
    )
    db.add(db_compra)
    db.commit()
    db.refresh(db_compra)
    return {"Missatge": "Compra creada correctament"}

def update_compra(
    id_compra: int,
    proveïdor: str,
    productes: str,
    quantitat_producte: int,
    preu_producte: int,
    preu_total: int,
    data_compra: str,
    db: Session
):
    sql_select = select(Compra).where(Compra.id_compra == id_compra)
    compra_db = db.exec(sql_select).one()

    compra_db.proveïdor = proveïdor
    compra_db.productes = productes
    compra_db.quantitat_producte = quantitat_producte
    compra_db.preu_producte = preu_producte
    compra_db.preu_total = preu_total
    compra_db.data_compra = data_compra

    db.add(compra_db)
    db.commit()
    db.refresh(compra_db)
    return {"Missatge": "Compra actualitzada correctament"}

def update_compra_field(id_compra: int, data: dict, db: Session):
    sql_select = select(Compra).where(Compra.id_compra == id_compra)
    compra_db = db.exec(sql_select).one_or_none()

    if not compra_db:
        return None

    for key, value in data.items():
        if hasattr(compra_db, key) and key != "id_compra":
            setattr(compra_db, key, value)

    db.add(compra_db)
    db.commit()
    db.refresh(compra_db)
    return {"Missatge": "Camp(s) de la compra actualitzat(s) correctament"}

def delete_compra(id_compra: int, db: Session):
    sql_select = select(Compra).where(Compra.id_compra == id_compra)
    compra_db = db.exec(sql_select).one()

    db.delete(compra_db)
    db.commit()
    return {"Missatge": "Compra esborrada correctament"}
#-----------------------------final-taula-Compra------------------------------------------------#