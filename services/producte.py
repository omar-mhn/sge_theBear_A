from schema.producte_sch import productes_schema
from sqlmodel import Session, select
from models.Producte import Producte

def get_all_productes(db: Session):
    sql_read = select(Producte)
    productes = db.exec(sql_read).all()
    return productes_schema(productes)

def get_producte(id_producte: int, db: Session):
    sql_read = select(Producte).where(Producte.id_producte == id_producte)
    producte = db.exec(sql_read).one()
    return productes_schema([producte])

def add_new_producte(id_producte: int, cost: float, quantitat: int, nom_producte: str, id_proveidor: int, id_prestatgeria: int, db: Session):
    db_producte = Producte(
        id_producte=id_producte,
        cost=cost,
        quantitat=quantitat,
        nom_producte=nom_producte,
        id_proveidor=id_proveidor,
        id_prestatgeria=id_prestatgeria
    )
    db.add(db_producte)
    db.commit()
    db.refresh(db_producte)
    return {"Missatge": "Producte creat correctament"}

def update_producte(id_producte: int, cost: float, quantitat: int, nom_producte: str, id_proveidor: int, id_prestatgeria: int, db: Session):
    sql_select = select(Producte).where(Producte.id_producte == id_producte)
    producte_db = db.exec(sql_select).one()

    producte_db.cost = cost
    producte_db.quantitat = quantitat
    producte_db.nom_producte = nom_producte
    producte_db.id_proveidor = id_proveidor
    producte_db.id_prestatgeria = id_prestatgeria

    db.add(producte_db)
    db.commit()
    db.refresh(producte_db)
    return {"Missatge": "Producte actualitzat correctament"}

def delete_producte(id_producte: int, db: Session):
    sql_select = select(Producte).where(Producte.id_producte == id_producte)
    producte_db = db.exec(sql_select).one()

    db.delete(producte_db)
    db.commit()
    return {"Missatge": "Producte esborrat correctament"}

def update_producte_field(id_producte: int, data: dict, db: Session):
    sql_select = select(Producte).where(Producte.id_producte == id_producte)
    producte_db = db.exec(sql_select).one_or_none()

    if not producte_db:
        return None

    for key, value in data.items():
        if hasattr(producte_db, key) and key != "id_producte":
            setattr(producte_db, key, value)

    db.add(producte_db)
    db.commit()
    db.refresh(producte_db)
    return {"Missatge": "Camp(s) actualitzat(s) correctament"}
