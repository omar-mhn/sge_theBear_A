from schema.producte_sch import productes_schema
from sqlmodel import Session, select
from models.Producte import Producte

def get_all_productes(db: Session):
    sql_read = select(Producte)
    productes = db.exec(sql_read).all()
    return productes_schema(productes)

def get_producte(id_producte: str, db: Session):
    sql_read = select(id_producte).where(Producte.id_producte == id_producte)
    producte = db.exec(sql_read).one()
    return productes_schema([producte])

def add_new_producte(id_producte: str, cost: str, quantitat: str, nom_producte: str, id_proveidor: str, id_prestatgeria: str, db: Session):
    db_producte = Producte(
        id_producte=id_producte,
        cost=cost,
        quantitat=quantitat,
        nom_producte=nom_producte,
        Id_proveidor=id_proveidor,
        Id_prestatgeria=id_prestatgeria
    )
    db.add(db_producte)
    db.commit()
    db.refresh(db_producte)
    return {"Message": "Created product successfully"}

def update_producte(id_producte: str, cost: str, quantitat: str, nom_producte: str, id_proveidor: str, id_prestatgeria: str, db: Session):
    sql_select = select(id_producte).where(Producte.id_producte == id_producte)
    producte_db = db.exec(sql_select).one()

    producte_db.id_producte = id_producte
    producte_db.cost = cost
    producte_db.quantitat = quantitat
    producte_db.nom_producte = nom_producte
    producte_db.id_proveidor = id_proveidor
    producte_db.id_prestatgeria = id_prestatgeria
    db.add(producte_db)
    db.commit()
    return {"msg": "Updated product successfully"}

def delete_producte(id_producte: str, db: Session):
    sql_select = select(id_producte).where(Producte.id_producte == id_producte)
    producte_db = db.exec(sql_select).one()

    db.delete(producte_db)
    db.commit()
    return {"Msg": "Product deleted successfully"}
