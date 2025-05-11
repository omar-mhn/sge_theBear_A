from decimal import Decimal

from schema.vendes_sch import vendes_schema
from sqlmodel import Session, select
from models.Vendre import Vendre
from decimal import Decimal

#--------------------------------taula-Venta---------------------------------------------------#

def get_all_compres(db: Session):
    sql_read = select(Vendre)
    vendes = db.exec(sql_read).all()
    return vendes_schema(vendes)

def get_compres(id_compra: int, db: Session):
    sql_read = select(Vendre).where(Vendre.id_compra == id_compra)
    venta = db.exec(sql_read).one()
    return venta.dict()

def add_create_compres(id_compra: int, cost_total: Decimal, data_comanda: str, db: Session):
    db_venta = Vendre(
        id_compra=id_compra,
        cost_total=cost_total,
        data_comanda=data_comanda
    )
    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)
    return {"Missatge": "Venta creada correctament"}

def update_compres(
    id_compra: int,
    cost_total: float,
    data_comanda: str,
    db: Session
):
    sql_select = select(Vendre).where(Vendre.id_compra == id_compra)
    venta_db = db.exec(sql_select).one()

    venta_db.cost_total = cost_total
    venta_db.data_comanda = data_comanda

    db.add(venta_db)
    db.commit()
    db.refresh(venta_db)
    return {"Missatge": "Venta actualitzada correctament"}

def update_compres_field(id_compra: int, data: dict, db: Session):
    sql_select = select(Vendre).where(Vendre.id_compra == id_compra)
    venta_db = db.exec(sql_select).one_or_none()

    if not venta_db:
        return None

    for key, value in data.items():
        if hasattr(venta_db, key) and key != "id_compra":
            setattr(venta_db, key, value)

    db.add(venta_db)
    db.commit()
    db.refresh(venta_db)
    return {"Missatge": "Camp(s) de la venta actualitzat(s) correctament"}

def delete_compres(id_compra: int, db: Session):
    sql_select = select(Vendre).where(Vendre.id_compra == id_compra)
    venta_db = db.exec(sql_select).one()

    db.delete(venta_db)
    db.commit()
    return {"Missatge": "Venta esborrat correctament"}

#-----------------------------final-taula-Venta------------------------------------------------#