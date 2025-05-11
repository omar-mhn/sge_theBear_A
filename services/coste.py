from schema.coste_sch import costes_schema
from sqlmodel import Session, select
from models.Coste import Coste

def get_all_costes(db: Session):
    sql_read = select(Coste)
    costes = db.exec(sql_read).all()
    return costes_schema(costes)

def get_coste(id_factura: int, db: Session):
    sql_read = select(Coste).where(Coste.id_factura == id_factura)
    coste = db.exec(sql_read).one()
    return coste.dict()

def add_new_coste(id_factura: int, data: str, tipus_cost: str, cost_total: int, id_compra: int, id_empleat: int, id_comanda: int, db: Session):
    db_coste = Coste(
        id_factura=id_factura,
        data=data,
        tipus_cost=tipus_cost,
        cost_total=cost_total,
        id_compra=id_compra,
        id_empleat=id_empleat,
        id_comanda=id_comanda
    )
    db.add(db_coste)
    db.commit()
    db.refresh(db_coste)
    return {"Missatge": "Cost afegit correctament"}

def update_coste(id_factura: int, data: str, tipus_cost: str, cost_total: int, id_compra: int, id_empleat: int, id_comanda: int, db: Session):
    sql_select = select(Coste).where(Coste.id_factura == id_factura)
    coste_db = db.exec(sql_select).one()

    coste_db.data = data
    coste_db.tipus_cost = tipus_cost
    coste_db.cost_total = cost_total
    coste_db.id_compra = id_compra
    coste_db.id_empleat = id_empleat
    coste_db.id_comanda = id_comanda

    db.add(coste_db)
    db.commit()
    db.refresh(coste_db)
    return {"Missatge": "Cost actualitzat correctament"}

def delete_coste(id_factura: int, db: Session):
    sql_select = select(Coste).where(Coste.id_factura == id_factura)
    coste_db = db.exec(sql_select).one()

    db.delete(coste_db)
    db.commit()
    return {"Missatge": "Cost esborrat correctament"}

def update_coste_field(id_factura: int, data: dict, db: Session):
    sql_select = select(Coste).where(Coste.id_factura == id_factura)
    coste_db = db.exec(sql_select).one_or_none()

    if not coste_db:
        return None

    for key, value in data.items():
        if hasattr(coste_db, key) and key != "id_factura":
            setattr(coste_db, key, value)

    db.add(coste_db)
    db.commit()
    db.refresh(coste_db)
    return {"Missatge": "Camp(s) actualitzat(s) correctament"}
