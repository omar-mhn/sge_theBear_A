from schema.coste_sch import costes_schema
from sqlmodel import Session, select
from models.Coste import Coste

def get_all_costes(db: Session):
    sql_read = select(Coste)
    costes = db.exec(sql_read).all()
    return costes_schema(costes)

def get_coste(id_factura: str, db: Session):
    sql_read = select(id_factura).where(Coste.id_factura == id_factura)
    coste = db.exec(sql_read).one()
    return costes_schema([coste])

def add_new_coste(id_factura: str, data: str, tipus_cost: str, cost_total: str, id_compra: str, id_empleat: str, id_comanda: str, db: Session):
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
    return {"Message": "Created cost successfully"}

def update_coste(id_factura: str, data: str, tipus_cost: str, cost_total: str, id_compra: str, id_empleat: str, id_comanda: str, db: Session):
    sql_select = select(id_factura).where(Coste.id_factura == id_factura)
    coste_db = db.exec(sql_select).one()

    coste_db.id_factura = id_factura
    coste_db.data = data
    coste_db.tipus_cost = tipus_cost
    coste_db.cost_total = cost_total
    coste_db.id_compra = id_compra
    coste_db.id_empleat = id_empleat
    coste_db.id_comanda = id_comanda
    db.add(coste_db)
    db.commit()
    return {"msg": "Updated cost successfully"}

def delete_coste(id_factura: str, db: Session):
    sql_select = select(id_factura).where(Coste.id_factura == id_factura)
    coste_db = db.exec(sql_select).one()

    db.delete(coste_db)
    db.commit()
    return {"Msg": "Cost deleted successfully"}
